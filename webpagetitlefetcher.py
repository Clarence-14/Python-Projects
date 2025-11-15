# A program that fetches and displays the title of a webpage using the requests and beautifulsoup4 libraries.

import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract the title
        title = soup.title.string if soup.title else "No title found"
        
        # Extract all hyperlinks
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        
        return title, links
    
    except requests.exceptions.RequestException as e:
        return f"Network error: {e}", []

# --- Interactive part ---
if __name__ == "__main__":
    url = input("Enter a webpage URL (e.g., https://example.com): ")
    title, links = get_page_title(url)
    
    print(f"\nPage Title: {title}")
    print("\nHyperlinks found on the page:")
    if links:
        for link in links:
            print(link)
    else:
        print("No hyperlinks found.")
