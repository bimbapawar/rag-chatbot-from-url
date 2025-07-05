import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    """
    Fetches and extracts clean text content from a given URL.
    
    Args:
        url (str): The webpage URL to scrape.

    Returns:
        str: Cleaned textual content from the page.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove unwanted tags like script and style
        for script_or_style in soup(['script', 'style', 'noscript']):
            script_or_style.decompose()

        text = soup.get_text(separator=' ')
        clean_text = ' '.join(text.split())  # Collapse whitespace
        return clean_text

    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch URL: {e}")
        return "Error: Unable to fetch content from the provided URL."
