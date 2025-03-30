import os

# Specify the LLM model to use. You can choose any LLM supported by LiteLLM.
# Example options include "gpt-4o", "claude", "deepseek-chat", etc.
# For a full list of supported models, refer to:
# https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
LLM_MODEL = "gemini/gemini-2.0-flash"

# API token for authentication with the LLM provider.
# This is fetched from the environment variable "GEMINI_API_KEY".
API_TOKEN = os.getenv("GEMINI_API_KEY")

# Base URL of the website to scrape.
# In this example, we are scraping Yellow Pages for dentists in Toronto, ON.
# You can modify the URL to change the location or the type of business.
# Example:
# - For plumbers in Vancouver: "https://www.yellowpages.ca/search/si/{page_number}/Plumbers/Vancouver+BC"
# - For restaurants in Montreal: "https://www.yellowpages.ca/search/si/{page_number}/Restaurants/Montreal+QC"
BASE_URL = "https://www.yellowpages.ca/search/si/{page_number}/Dentists/Toronto+ON"

# CSS selector to target the main HTML element containing the business information.
# This is specific to Yellow Pages and helps focus the scraper on relevant content
# instead of sending the entire HTML page to the LLM.
CSS_SELECTOR = "[class^='listing_right_section']"

# Maximum number of pages to crawl. Adjust this value based on how much data you want to scrape.
MAX_PAGES = 3  # Example: Set to 5 to scrape 5 pages.

# Instructions for the LLM on what information to extract from the scraped content.
# The LLM will extract the following details for each business:
# - Name
# - Address
# - Website
# - Phone number
# - A one-sentence description
SCRAPER_INSTRUCTIONS = (
    "Extract all business information: 'name', 'address', 'website'"
    ", 'phone number' and a one-sentence 'description' from the following content."
)