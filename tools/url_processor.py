from langchain.tools import BaseTool
import requests
from bs4 import BeautifulSoup

class URLProcessorTool(BaseTool):
    name = "url_processor"
    description = "Process webpage URLs to extract content"
    
    def _run(self, url: str):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text(separator=' ', strip=True)[:2000]
        except Exception as e:
            return f"Error processing URL: {str(e)}"