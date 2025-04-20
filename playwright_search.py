from playwright.sync_api import sync_playwright
import time

def search_amazon():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
        page = browser.new_page()
        
        try:
            # Navigate to Amazon
            print("Navigating to Amazon...")
            page.goto('https://www.amazon.com')
            
            # Wait for the search box to be visible
            print("Waiting for search box...")
            search_box = page.locator('input#twotabsearchtextbox')
            search_box.wait_for()
            
            # Type the search query
            print("Typing search query...")
            search_box.fill('The Goal by Eliyahu M. Goldratt')
            
            # Press Enter
            print("Performing search...")
            search_box.press('Enter')
            
            # Wait for search results
            print("Waiting for search results...")
            page.wait_for_selector('div[data-component-type="s-search-result"]')
            
            # Click the first result
            print("Clicking first result...")
            first_result = page.locator('div[data-component-type="s-search-result"]').first
            first_result.click()
            
            # Keep the browser open for a while to see the result
            print("Keeping browser open for 30 seconds...")
            time.sleep(30)
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            # Close the browser
            browser.close()

if __name__ == "__main__":
    search_amazon() 