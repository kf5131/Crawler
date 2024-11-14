from bs4 import BeautifulSoup

from utils import *

def get_page_soup(url: str = "https://www.google.com"):
    return BeautifulSoup(get_page_content(url), 'lxml')

def parse_page(url: str = "https://www.google.com"):
    soup = get_page_soup(url)

    return {
        "links": get_links(soup),
        "images": get_images(soup),
        "text": get_text(soup),
        "title": get_title(soup),
        "meta": {
            "description": get_meta_description(soup),
            "keywords": get_meta_keywords(soup),
            "robots": get_meta_robots(soup),
            "viewport": get_meta_viewport(soup),
            "author": get_meta_author(soup),
            "generator": get_meta_generator(soup)
        }
    }


def get_links(soup: BeautifulSoup) -> list[str]:
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def get_images(soup: BeautifulSoup) -> list[str]:
    images = []
    for image in soup.find_all('img'):
        images.append(image.get('src'))
    return images

def get_text(soup: BeautifulSoup) -> str:
    return soup.get_text()

def get_title(soup: BeautifulSoup) -> str:
    return soup.title.string

def get_meta_description(soup: BeautifulSoup) -> str | None:
    meta = soup.find('meta', {'name': 'description'})
    return meta.get('content') if meta else None

def get_meta_keywords(soup: BeautifulSoup) -> str | None:
    meta = soup.find('meta', {'name': 'keywords'})
    return meta.get('content') if meta else None

def get_meta_robots(soup: BeautifulSoup) -> str | None:
    meta = soup.find('meta', {'name': 'robots'})
    return meta.get('content') if meta else None

def get_meta_viewport(soup: BeautifulSoup) -> str | None:
    meta = soup.find('meta', {'name': 'viewport'})
    return meta.get('content') if meta else None

def get_meta_author(soup: BeautifulSoup) -> str | None:
    meta = soup.find('meta', {'name': 'author'})
    return meta.get('content') if meta else None

def get_meta_generator(soup: BeautifulSoup) -> str | None:
    meta = soup.find('meta', {'name': 'generator'})
    return meta.get('content') if meta else None


if __name__ == "__main__":
    parse_page()

