import os
from playwright.sync_api import sync_playwright
import json
import csv
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def search_dentist_info(page, city):
    # Navigate to Gemini
    page.goto('https://gemini.google.com/')
    
    # Wait for the chat input to be ready
    page.wait_for_selector('textarea[placeholder*="Message"]')
    
    # Prepare the prompt
    prompt = f"""
    Search for dentists in {city}, Utah and provide specific information.
    
    For each dentist you find, provide the following information in JSON format:
    {{
        "name": "Full name of the dentist",
        "email": "Their email address",
        "address": "Complete physical address",
        "practice_name": "Name of their dental practice"
    }}
    
    Important rules:
    1. Only include dentists where you can find ALL the required information
    2. Do not include generic or placeholder information
    3. Verify the information is current and accurate
    4. Search through dental association websites, business directories, and official practice websites
    5. Return up to 5 complete entries
    6. Format the response as a JSON array of objects
    
    Example of valid entry:
    {{
        "name": "Dr. John Smith",
        "email": "dr.smith@example.com",
        "address": "123 Main St, {city}, UT 84000",
        "practice_name": "Smith Family Dentistry"
    }}
    
    If you cannot find complete information for a dentist, do not include them in the results.
    """
    
    # Type the prompt
    page.fill('textarea[placeholder*="Message"]', prompt)
    page.press('textarea[placeholder*="Message"]', 'Enter')
    
    # Wait for the response
    page.wait_for_selector('div[data-message-author="model"]')
    
    # Get the response text
    response = page.query_selector('div[data-message-author="model"]').inner_text()
    
    try:
        # Try to parse the JSON response
        data_list = json.loads(response)
        return data_list
    except json.JSONDecodeError:
        print(f"Could not parse response for {city}")
        return None

def save_to_csv(data_list, filename='utah_dentists.csv'):
    # Create or append to CSV file
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['name', 'email', 'address', 'practice_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if file is new
        if not file_exists:
            writer.writeheader()
        
        # Write data
        for data in data_list:
            writer.writerow(data)

def main():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # List of Utah cities to search in
        cities = [
            'Salt Lake City', 'Provo', 'Ogden', 'St. George', 'Orem',
            'Layton', 'South Jordan', 'Sandy', 'West Jordan', 'Lehi'
        ]
        
        for city in cities:
            print(f"\nSearching for dentists in {city}...")
            
            try:
                # Get dentist information for the city
                data_list = search_dentist_info(page, city)
                
                if data_list and isinstance(data_list, list):
                    save_to_csv(data_list)
                    print(f"Saved {len(data_list)} dentists from {city}")
                else:
                    print(f"No valid dentist information found for {city}")
                
                time.sleep(5)  # Rate limiting between cities
                    
            except Exception as e:
                print(f"Error processing {city}: {str(e)}")
        
        browser.close()

if __name__ == "__main__":
    main() 