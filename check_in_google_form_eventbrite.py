import argparse
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


def login_to_eventbrite(driver, email, password):
    """Log in to Eventbrite."""
    print(Fore.BLUE + "Navigating to Eventbrite login page...")
    driver.get("https://www.eventbrite.com/login/")
    time.sleep(2)

    try:
        # Enter email and password, then click login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()

        print(Fore.BLUE + "Waiting for login to complete...")
        time.sleep(5)  # Wait for login to complete
        print(Fore.GREEN + "Successfully logged in.")
    except Exception as e:
        print(Fore.RED + f"Login failed: {e}")
        save_page_source(driver, "login_error_page.html")
        raise


def check_in_attendees(driver, checkin_url, attendees):
    """Navigate to the check-in page and check in attendees."""
    print(Fore.BLUE + "Navigating to the check-in page...")
    driver.get(checkin_url)
    time.sleep(5)

    for attendee_email in attendees:
        try:
            print(Fore.YELLOW + f"Processing attendee: {attendee_email}")

            # Search for the attendee
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "checkin_table_filter_input"))
            )
            search_input.clear()
            search_input.send_keys(attendee_email)
            time.sleep(3)  # Allow search results to load

            # Save the current page source for debugging
            save_page_source(driver, f"logs/debug_{attendee_email}.html")

            # Locate attendee rows dynamically
            search_results = driver.find_elements(By.XPATH, '//div[contains(@class, "responsive-table--stacked__content")]/span[@title]')
            print(Fore.CYAN + f"Debug: Found {len(search_results)} attendee rows for {attendee_email}.")
            
            if len(search_results) == 0:
                print(Fore.RED + f"No attendee found with email: {attendee_email}. Skipping...")
                continue

            # Check if attendee is already checked in
            is_checked_in = False
            for result in search_results:
                attendee_name = result.get_attribute("title")
                print(Fore.YELLOW + f"Checking attendee name: {attendee_name}")
                
                # Locate the check-in status
                check_in_status = driver.find_elements(By.XPATH, f'//i[contains(@class, "ico-checkmark") and contains(@id, "checkin_button_")]')
                if check_in_status:
                    is_checked_in = True
                    print(Fore.GREEN + f"Attendee {attendee_email} is already checked in. Skipping...")
                    break

            if is_checked_in:
                continue

            # Proceed to check-in if not already checked in
            print(Fore.BLUE + f"Attendee {attendee_email} is not checked in. Proceeding...")
            check_in_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "checkin_button") and text()="Check in"]'))
            )
            check_in_button.click()
            print(Fore.GREEN + f"Checked in: {attendee_email}")
            time.sleep(2)
        except Exception as e:
            print(Fore.RED + f"Error processing {attendee_email}: {e}")
            save_page_source(driver, f"logs/error_{attendee_email}.html")



def save_page_source(driver, filename):
    """Save the current page source to a file for debugging."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(Fore.CYAN + f"Saved page source to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Automate Eventbrite check-in process.")
    parser.add_argument("--email", required=True, help="Eventbrite login email")
    parser.add_argument("--password", required=True, help="Eventbrite login password")
    parser.add_argument("--event_id", required=True, help="Eventbrite Event ID")
    parser.add_argument("--attendees_csv", required=True, help="Path to the attendees CSV file")

    args = parser.parse_args()

    # Construct the check-in URL dynamically using the event ID
    checkin_url = f"https://www.eventbrite.com/checkin?eid={args.event_id}"

    # Load attendees from the CSV file
    attendees_df = pd.read_csv(args.attendees_csv)
    attendees = attendees_df["Email"].tolist()
    print(Fore.CYAN + f"Loaded {len(attendees)} attendees from {args.attendees_csv}.")

    # Set up the WebDriver with headless mode as default
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximize window for visibility
    options.add_argument("--headless=new")  # Enable headless mode by default
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--no-sandbox")  # Required for some environments
    options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Log in and check in attendees
        print(Fore.BLUE + "Logging in to Eventbrite...")
        login_to_eventbrite(driver, args.email, args.password)

        print(Fore.BLUE + f"Checking in attendees for Event ID: {args.event_id}")
        check_in_attendees(driver, checkin_url, attendees)
        print(Fore.GREEN + "All attendees processed.")
    finally:
        driver.quit()
        print(Fore.CYAN + "Browser closed. Process completed.")


if __name__ == "__main__":
    main()
