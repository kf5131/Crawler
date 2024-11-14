# Utility functions

import requests

def get_page_content(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

def get_url_from_user() -> str:
    url = input("Enter the URL to parse: ")
    if not url:
        url = "https://www.google.com"
        print("Warning: URL cannot be empty")
    if not url.startswith("http"):
        url = "https://" + url
    return url
