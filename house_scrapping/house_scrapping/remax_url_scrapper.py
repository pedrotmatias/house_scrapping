import json
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse

class RemaxURLScraper:
    """
    A class for scraping listing URLs from REMAX website based on user-defined search parameters.
    """

    def __init__(self):
        """
        Initialize the RemaxWebScraper instance.
        """
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.base_url = "https://www.remax.pt/comprar"
        self.search_params = {
            "regionName": "",
            "businessType": 1,
            "listingClass": 1,
            "page": 1,
            "sort": {
                "fieldToSort": "PublishDate",
                "order": 1
            },
            "listingTypes": ["1", "5", "11", "12", "3", "24", "13"],
            "mapScroll": False,
            "price": {
                "min": 70000,
                "max": 300000
            },
            "rooms": 2,
            "hasMultimedia": False,
            "isOpportunity": False,
            "isMultipleProposal": False,
            "bathrooms": 1
        }
        
    def set_search_param(self, param_name, param_value):
        """
        Set the value of a search parameter.

        Args:
            param_name (str): The name of the parameter to set.
            param_value (object): The new value for the parameter.
        """
        if param_name in self.search_params:
            self.search_params[param_name] = param_value
        else:
            print(f"Invalid search parameter: {param_name}")

    def construct_search_url(self):
        """
        Construct the search URL using the current search parameters.

        Returns:
            str: The constructed search URL.
        """
        encoded_params = urllib.parse.quote(json.dumps(self.search_params))
        return f"{self.base_url}?searchQueryState={encoded_params}"

    def scrape_listing_urls(self, search_url):
        """
        Scrape listing URLs based on the current search parameters.

        Returns:
            list: A list of scraped listing URLs.
        """
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(search_url)
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, 'html.parser')
        listings_container = soup.find('div', 'listing-search-searchresults-component')

        listings = listings_container.find_all('div', class_='listing-search-searchdetails-component')
        listing_urls = []

        for listing in listings:
            anchor_tag = listing.find('a')
            if anchor_tag:
                href = anchor_tag['href']
                full_url = 'https://remax.pt' + href
                listing_urls.append(full_url)

        return listing_urls

if __name__ == "__main__":
    scraper = RemaxURLScraper()

    # Modify search parameters as needed
    scraper.set_search_param("rooms", 3)
    search_url = scraper.construct_search_url()
    print( search_url )
    # listing_urls_variation_1 = scraper.scrape_listing_urls( search_url )
    # for url in listing_urls_variation_1:
    #     print("Listing URL (Variation 1):", url)

    # Modify other parameters as needed
    scraper.set_search_param("price", {"min": 80000, "max": 250000})
    search_url2 = scraper.construct_search_url( )
    print( search_url2 )
    listing_urls_variation_2 = scraper.scrape_listing_urls( search_url2 )
    for url in listing_urls_variation_2:
        print("Listing URL (Variation 2):", url)
