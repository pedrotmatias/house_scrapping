import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class HouseInfoScraper:
    """
    A class for scraping house information from a website and storing it in a dictionary.
    """

    def __init__(self, url):
        """
        Initialize the HouseInfoScraper instance.

        Args:
            url (str): The URL of the house listing.
        """
        self.url = url
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.driver = None
        self.house = {}
        self.scrap_house()

    def _get_driver(self):
        """
        Initialize the Chrome WebDriver if not already initialized.
        """
        if self.driver is None:
            self.driver = webdriver.Chrome(options=self.chrome_options)

    def _close_driver(self):
        """
        Close the Chrome WebDriver if it's open.
        """
        if self.driver:
            self.driver.quit()
            self.driver = None

    def scrap_house(self):
        """
        Scrap house information from the website and populate the house dictionary.
        """
        self._get_driver()
        self.driver.get(self.url)
        html = self.driver.page_source
        self._close_driver()

        soup = BeautifulSoup(html, 'html.parser')
        self._scrap_location_info(soup)
        self._scrap_top_info(soup)
        self._scrap_remax_table(soup)

    def _scrap_location_info(self, soup):
        """
        Scrap and store location information from the website.

        Args:
            soup (BeautifulSoup): The parsed HTML content.
        """
        location_elements = soup.find_all('h2', class_=lambda x: x and 'listing-address' in x.split())
        for location_element in location_elements:
            self.house["location"] = location_element.get_text(strip=True)

    def _scrap_top_info(self, soup):
        """
        Scrap and store top information of the house from the website.

        Args:
            soup (BeautifulSoup): The parsed HTML content.
        """
        top_info = soup.find('div', 'listing-top-info')
        self._scrap_price(top_info)
        self._scrap_id(top_info)

    def _scrap_price(self, top_info):
        """
        Scrap and store the price of the house.

        Args:
            top_info (Tag): The top information HTML tag.
        """
        price = top_info.find('span', 'listing-price')
        if price:
            self.house['price'] = price.string.replace(" ", "").replace("€", "")

    def _scrap_id(self, top_info):
        """
        Scrap and store the ID of the house.

        Args:
            top_info (Tag): The top information HTML tag.
        """
        id = top_info.find('span', 'listing-title')
        if id:
            self.house['id'] = id.string.replace(" ", "").replace("€", "")

    def _scrap_remax_table(self, soup):
        """
        Scrap and store table information of the house from the website.

        Args:
            soup (BeautifulSoup): The parsed HTML content.
        """
        remax_table = soup.find('div', {'id': 'tabs-navigation'})
        details = remax_table.find('div', {'id': 'details'})
        array_of_vals = []

        for value in details.find_all('td', class_=lambda x: x != 'first-column'):
            array_of_vals.append(value.text.replace(" ", "").replace("€", ""))

        if array_of_vals:
            labels = [
                'Private Building Area', 'Building Area', 'Total Area', 'Total Useful Area',
                'Number of Rooms', 'Year of construction', 'Floor', 'Number of WCs',
                'Elevator', 'Parking'
            ]
            for i, label in enumerate(labels):
                self.house[label] = array_of_vals[i]

    def get_house(self):
        """
        Get the house information dictionary.

        Returns:
            dict: The dictionary containing house information.
        """
        return self.house

if __name__ == '__main__':
    url = 'https://www.remax.pt/imoveis/venda-apartamento-t2-matosinhos-sao-mamede-de-infesta-e-senhora-da-hora/120781092-178'
    house = HouseInfoScraper(url)
    print(house.get_house())
