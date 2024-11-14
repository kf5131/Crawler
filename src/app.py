# CLI interface

import click

from crawler import *
from utils import *

@click.command()
def main():
    url = get_url_from_user()
    page_data = parse_page(url)

    print(page_data)



if __name__ == "__main__":
    main()
