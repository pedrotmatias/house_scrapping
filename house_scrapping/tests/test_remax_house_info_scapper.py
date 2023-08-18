import unittest
from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from selenium import webdriver
from house_scrapping.remax_house_info_scraper import HouseInfoScraper  # Replace with the actual module name

class TestHouseInfoScraper(unittest.TestCase):
    """
    Unit tests for the HouseInfoScraper class.
    """

    def setUp(self):
        """
        Set up common resources for test cases.
        """
        # Mocking the webdriver instance for testing
        self.mock_driver = MagicMock(spec=webdriver.Chrome)
        self.mock_driver.page_source = '<html><body></body></html>'
        self.mock_driver.get.return_value = None

    def test_scrap_location_info(self):
        """
        Test the scrap_location_info method.
        """
        # Mock the BeautifulSoup instance for testing
        mock_soup = BeautifulSoup('<html><h2 class="listing-address">Location</h2></html>', 'html.parser')
        
        # Create a HouseInfoScraper instance
        scraper = HouseInfoScraper('http://example.com')
        scraper.driver = self.mock_driver
        scraper.scrap_location_info(mock_soup)

        self.assertEqual(scraper.house['location'], 'Location')

    def test_scrap_top_info(self):
        """
        Test the scrap_top_info method.
        """
        # Mock the BeautifulSoup instance for testing
        mock_soup = BeautifulSoup('<html><div class="listing-top-info"><span class="listing-price">100 €</span><span class="listing-title">123</span></div></html>', 'html.parser')

        # Create a HouseInfoScraper instance
        scraper = HouseInfoScraper('http://example.com')
        scraper.driver = self.mock_driver
        scraper.scrap_top_info(mock_soup)

        self.assertEqual(scraper.house['price'], '100')
        self.assertEqual(scraper.house['id'], '123')

    # Add more test methods for other functions

if __name__ == '__main__':
    unittest.main()
