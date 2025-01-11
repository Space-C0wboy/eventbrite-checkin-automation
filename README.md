# Automated Eventbrite Check-In Tool

Automates the attendee check-in process for Eventbrite events using Python and Selenium. This tool reads attendee emails from a CSV file, searches for them on the Eventbrite check-in page, checks their status, and marks them as checked in if they are not already.

## Features

- **Automated Check-In**: Marks attendees as checked in directly on the Eventbrite platform.
- **Check-In Status Detection**: Skips attendees who are already checked in and logs their status.
- **CSV Integration**: Reads attendee emails from a provided CSV file.
- **Detailed Logging**: Generates verbose logs, including debug information, in a `logs/` directory.
- **Headless Mode**: Runs the script in headless mode by default for automation environments.
- **Error Handling**: Handles login and attendee processing errors gracefully, saving debug information for troubleshooting.
- **Dynamic Check-In URL**: Automatically constructs the check-in URL based on the provided Eventbrite event ID.

## Prerequisites

- Python 3.7 or later
- Google Chrome browser
- ChromeDriver (managed automatically via `webdriver-manager`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Space-C0wboy/eventbrite-checkin-automation.git
   cd eventbrite-checkin-automation
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your CSV file with a column labeled `Email`, containing the email addresses of attendees.

2. Run the script with the required arguments:
   ```bash
   python check_in_google_form_eventbrite.py --email YOUR_EVENTBRITE_EMAIL --password YOUR_EVENTBRITE_PASSWORD --event_id YOUR_EVENT_ID --attendees_csv YOUR_CSV_FILE
   ```

   Example:
   ```bash
   python check_in_google_form_eventbrite.py --email email@email.com --password mysupercoolpassword --event_id ########### --attendees_csv attendees.csv
   ```

3. The script will:
   - Log in to Eventbrite.
   - Check the status of each attendee.
   - Skip already checked-in attendees.
   - Check in attendees not yet marked as checked in.
   - Handle errors and save debug information in the `logs/` folder.

## Arguments

- `--email`: Your Eventbrite login email.
- `--password`: Your Eventbrite login password.
- `--event_id`: The Eventbrite event ID.
- `--attendees_csv`: Path to the CSV file containing attendee emails.
- **New Arguments:**
  - `--headless`: Optional. Enables or disables headless mode (default is enabled). To disable headless mode, pass `--headless false`.
  - `--verbose`: Optional. Increases log verbosity for debugging purposes.

## Logs

- Logs are saved in a `logs/` directory with detailed information about processing, errors, and debug outputs.
- Debug logs are created for each attendee processed, showing the state of the check-in page for troubleshooting.

## Troubleshooting

- **Login Issues**: Verify your credentials and ensure the Eventbrite login page structure hasn’t changed. A debug log of the login page is saved in the `logs/` folder.
- **Attendees Not Found**: Ensure the email addresses in the CSV file match those on Eventbrite. Debug logs are saved for attendees that could not be found.
- **Headless Errors**: If running headless causes issues, disable headless mode by passing `--headless false`.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
