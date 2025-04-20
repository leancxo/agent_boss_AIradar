from playwright.sync_api import sync_playwright
import time
import random

def random_delay(min_seconds=1, max_seconds=3):
    time.sleep(random.uniform(min_seconds, max_seconds))

def grocery_shopping():
    # List of items to add to cart
    items_to_buy = [
        "milk",
        "bread",
        "eggs",
        "bananas"
    ]
    
    with sync_playwright() as p:
        # Launch the browser with stealth settings
        browser = p.chromium.launch(
            headless=False,
            args=[
                '--start-maximized',
                '--disable-blink-features=AutomationControlled',
                '--disable-automation'
            ]
        )
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            has_touch=True,
            locale='en-US',
            timezone_id='America/New_York'
        )
        
        # Add human-like behaviors
        context.set_default_timeout(60000)  # Increase timeout to 60 seconds
        page = context.new_page()
        
        try:
            # Navigate to Instacart
            print("Navigating to Instacart...")
            page.goto('https://www.instacart.com')
            random_delay()
            
            # Wait for and click the shop button
            print("Looking for store selection...")
            shop_button = page.locator('button:has-text("Start shopping")')
            shop_button.wait_for()
            random_delay()
            shop_button.click()
            
            # Process each item
            for item in items_to_buy:
                print(f"\nSearching for {item}...")
                
                # Find and click the search box
                search_box = page.locator('input[placeholder*="Search"]')
                search_box.wait_for()
                random_delay()
                search_box.click()
                
                # Type the search query with random delays between characters
                for char in item:
                    search_box.type(char, delay=random.uniform(100, 300))
                random_delay(0.5, 1)
                search_box.press('Enter')
                
                # Wait for search results
                print(f"Waiting for {item} search results...")
                page.wait_for_selector('button[aria-label*="Add to cart"]')
                random_delay()
                
                # Click add to cart on the first result
                print(f"Adding {item} to cart...")
                add_button = page.locator('button[aria-label*="Add to cart"]').first
                add_button.click()
                random_delay()
                
            # View cart
            print("\nGoing to cart...")
            cart_button = page.locator('a[href*="cart"]')
            cart_button.click()
            
            # Keep the browser open to see the cart
            print("Keeping browser open for 30 seconds...")
            time.sleep(30)
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            # Close the browser
            browser.close()

if __name__ == "__main__":
    grocery_shopping() 