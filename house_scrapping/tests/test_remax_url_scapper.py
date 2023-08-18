import unittest
from house_scrapping.remax_url_scrapper import RemaxURLScraper

class TestRemaxWebScraper(unittest.TestCase):
    def test_set_search_param(self):
        """Test if the set_search_param method correctly updates search parameters."""
        scraper = RemaxURLScraper()
        scraper.set_search_param("rooms", 3)
        self.assertEqual(scraper.search_params["rooms"], 3)

    def test_scrape_listing_urls(self):
        """Test if the scrape_listing_urls method returns valid listing URLs."""
        scraper = RemaxWebScraper()
        urls = scraper.scrape_listing_urls()
        
        # Check if the returned URLs are valid by verifying their format
        self.assertIsInstance(urls, list)
        self.assertTrue(all(url.startswith("https://remax.pt/") for url in urls))

if __name__ == '__main__':
    unittest.main()
