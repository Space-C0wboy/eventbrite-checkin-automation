# Automated Eventbrite Check-In Tool

Automates the attendee check-in process for Eventbrite events using Python and Selenium. This tool reads attendee emails from a CSV file, searches for them on the Eventbrite check-in page, checks their status, and marks them as checked in if they are not already.

## Features

- **Automated Check-In**: Marks attendees as checked in directly on the Eventbrite platform.
- **Check-In Status Detection**: Skips attendees who are already checked in.
- **CSV Integration**: Reads attendee emails from a provided CSV file.
- **Detailed Logging**: Generates logs for tracking progress and debugging issues.
- **Error Handling**: Gracefully handles errors and saves debug information for failed operations.

## Prerequisites

- Python 3.7 or later
- Google Chrome browser
- ChromeDriver (managed automatically via `webdriver-manager`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/eventbrite-checkin-automation.git
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

## Arguments

- `--email`: Your Eventbrite login email.
- `--password`: Your Eventbrite login password.
- `--event_id`: The Eventbrite event ID.
- `--attendees_csv`: Path to the CSV file containing attendee emails.

## Logs

Logs are saved in a `logs/` directory with detailed information about processing, errors, and debug outputs.

## Troubleshooting

- If login fails, verify your credentials and ensure the Eventbrite login page structure hasn’t changed.
- If attendees are not found, ensure the email addresses in the CSV file match those on Eventbrite.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

Replace `https://github.com/yourusername/eventbrite-checkin-automation.git` with your actual GitHub repository URL.
