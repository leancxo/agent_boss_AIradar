from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

async def main():
    try:
        # Initialize the agent with a very specific task
        agent = Agent(
            task="""1. Open a new browser window
2. Type 'amazon.com' in the address bar
3. Press Enter to navigate to Amazon
4. Wait for the page to fully load
5. Locate the search box at the top of the page
6. Click inside the search box
7. Type 'The Goal by Eliyahu M. Goldratt'
8. Press Enter to perform the search
9. Wait for the search results to load
10. Look for the first book result that contains 'The Goal' in its title
11. Click on that book result""",
            llm=ChatOpenAI(
                model="gpt-4",
                temperature=0.1  # Lower temperature for more deterministic behavior
            )
        )
        
        logger.info("Starting browser automation...")
        await agent.run()
        logger.info("Automation completed successfully")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main()) 