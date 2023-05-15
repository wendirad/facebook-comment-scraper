import argparse
import json
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FacebookCommentScraper:

    def __init__(self, driver: webdriver.Chrome, url: str):
        self.driver = driver
        self.url = url

    def scrape(self):
        raise NotImplementedError()


def main():
    # Process command line arguments
    parser = argparse.ArgumentParser(description='Process comment scraping from facebook post.')

    parser.add_argument('urls', metavar='url', type=str, nargs='+', help='Facebook post url')
    parser.add_argument('-o', '--output', metavar='output', type=str, help='Output file name')
    args = parser.parse_args()

    # Setup selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_extension('./extension_1_0_4_0.crx')
    
    driver = webdriver.Chrome(options=options)

    # Scrape comments
    datas = []

    for url in args.urls:
        scraper = FacebookCommentScraper(driver, url)
        datas += scraper.scrape()
        
    if args.output is not None:
        with open(args.output, 'w') as f:
            json.dump(datas, f, indent=2)
    else:
        sys.stdout.write(json.dumps(datas, indent=2))

    driver.quit()

if __name__ == '__main__':
    main()