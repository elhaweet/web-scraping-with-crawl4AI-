import asyncio
from crawl4ai import AsyncWebCrawler
from dotenv import load_dotenv
from config import BASE_URL, CSS_SELECTOR, MAX_PAGES, SCRAPER_INSTRUCTIONS
from src.utils import save_data_to_csv
from src.scraper import (
    get_browser_config,
    get_llm_strategy,
    fetch_and_process_page
)
from models.business import BusinessData

load_dotenv()


async def crawl_yellowpages():
    """
    Main function to crawl businesses data from the website.
    """
    # Initialize configurations
    browser_config = get_browser_config()
    llm_strategy = get_llm_strategy(
        llm_instructions=SCRAPER_INSTRUCTIONS,  # Instructions for the LLM
        output_format=BusinessData # Data output format
    )
    session_id = "crawler_session"

    # Initialize state variables
    page_number = 1
    all_records = []
    seen_names = set()

    # Start the web crawler context
    # https://docs.crawl4ai.com/api/async-webcrawler/#asyncwebcrawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        while True:
            # Fetch and process data from the current page
            records, no_results_found = await fetch_and_process_page(
                crawler,
                page_number,
                BASE_URL,
                CSS_SELECTOR,
                llm_strategy,
                session_id,
                seen_names,
            )

            if no_results_found:
                print("No more records found. Ending crawl.")
                break  # Stop crawling when "No Results Found" message appears

            if not records:
                print(f"No records extracted from page {page_number}.")
                break  # Stop if no records are extracted

            # Add the records from this page to the total list
            all_records.extend(records)
            page_number += 1  # Move to the next 
            
            if page_number > MAX_PAGES:
                break

            # Pause between requests to avoid rate limits
            await asyncio.sleep(2)  # Adjust sleep time as needed

    # Save the collected records to a CSV file
    if all_records:
        save_data_to_csv(
            records=all_records, 
            data_struct=BusinessData,
            filename="businesses_data.csv"
        )
    else:
        print("No records were found during the crawl.")

    # Display usage statistics for the LLM strategy
    llm_strategy.show_usage()


async def main():
    """
    Entry point of the script.
    """
    await crawl_yellowpages()


if __name__ == "__main__":
    asyncio.run(main())
