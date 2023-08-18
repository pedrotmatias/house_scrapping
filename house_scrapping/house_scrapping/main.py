from remax_house_info_scraper  import HouseInfoScraper
from remax_url_scrapper import RemaxURLScraper

# Create an instance of RemaxURLScraper
url_scraper = RemaxURLScraper()

# Modify search parameters as needed
url_scraper.set_search_param("rooms", 3)
listing_urls = url_scraper.scrape_listing_urls()

# Create an empty list to store house information dictionaries
house_info_list = []

# Iterate through the listing URLs and scrape house information
for url in listing_urls:
    house_scraper = HouseInfoScraper(url)
    house_info = house_scraper.get_house()
    house_info_list.append(house_info)

# Print the scraped house information
for idx, house_info in enumerate(house_info_list, start=1):
    print(f"House {idx} Information:")
    for key, value in house_info.items():
        print(f"{key}: {value}")
    print("=" * 40)
