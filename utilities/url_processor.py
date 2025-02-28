import requests
from bs4 import BeautifulSoup

def process_url(url: str) -> str:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text(separator=' ', strip=True)[:2000]
    except Exception as e:
        return f"Error processing URL: {str(e)}"