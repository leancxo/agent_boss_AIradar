# Utah Dentist Information Scraper

This project uses Google's Gemini API to search for dentist information in Utah and stores the data in a Google Sheet.

## Setup Instructions

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Google Cloud Project and enable APIs:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Google Sheets API
   - Create credentials (OAuth 2.0 Client ID)
   - Download the credentials and save as `credentials.json` in the project directory

3. Create a Google Sheet:
   - Create a new Google Sheet
   - Copy the Sheet ID from the URL (the long string between /d/ and /edit)
   - Add the following headers to the first row:
     - Name
     - Email
     - Address
     - Practice Name

4. Set up environment variables:
   Create a `.env` file in the project directory with the following variables:
   ```
   GOOGLE_API_KEY=your_gemini_api_key
   SPREADSHEET_ID=your_google_sheet_id
   ```

## Running the Script

Run the script using:
```bash
python dentist_scraper.py
```

The script will:
1. Search for dentists in major Utah cities
2. Collect specific information about each dentist
3. Store the information in the Google Sheet
4. Skip any entries with generic or incomplete information

## Notes

- The script includes rate limiting to avoid API restrictions
- Only complete entries (with all required information) will be added to the spreadsheet
- The script searches in 10 major Utah cities
- Each city will have up to 5 dentists processed 