# Path: house_scrapping\Scrapper.py
import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup

#This Class is responsible for scrapping the house information from the website
#The information is stored in a dictionary
class Scrapper:
    def __init__( self, url ):
       self.url = url
       self.driver = webdriver.Chrome()
       self.house = {}
       self.scrap_house()

    
    def scrap_house( self ):
       self.driver.get( self.url )
       html = self.driver.page_source
       soup = BeautifulSoup(html, 'html.parser')
       self.scrap_top_info( soup )
       self.scrap_remax_table( soup )
    
    #This function scraps the top information of the house
    #The top information is the price and the id of the house   
    def scrap_top_info( self, soup ):
        top_info = soup.find('div', 'listing-top-info')
        for info in top_info:
            price = top_info.find( 'span', 'listing-price' )
            self.house['price'] = price.string.replace(" ", "").replace("€","")

        for info in top_info:
            id = top_info.find( 'span', 'listing-title' )
            self.house['id'] = id.string.replace(" ", "").replace("€","")
            
    #This function scraps the table with the house information
    #The information is stored in a dictionary
    def scrap_remax_table( self, soup ):
        remax_table = soup.find( 'div' , { 'id' : 'tabs-navigation'} )
        details = remax_table.find( 'div', {'id' : 'details'} )
        array_of_vals = []
        for value in details.find_all( 'td', class_=lambda x: x != 'first-column' ):
            array_of_vals.append( value.text.replace(" ", "").replace("€","") )

        if array_of_vals:
            self.house['Private Building Area'] = array_of_vals[0]
            self.house['Building Area'] = array_of_vals[1]
            self.house['Total Area'] = array_of_vals[2]
            self.house['Total Useful Area'] = array_of_vals[3]
            self.house['Number of Rooms'] = array_of_vals[4]
            self.house['Year of construction'] = array_of_vals[ 5 ]
            self.house['Floor'] = array_of_vals [6]
            self.house['Number of WCs'] = array_of_vals [7]
            self.house['Elevator'] = array_of_vals [8]
            self.house['Parking'] = array_of_vals [9]
            
    #
    def print_house( self ):
        for items in self.house.items():
            print( items)
    
    #This function returns the house dictionary        
    def get_house( self ):
        return self.house
    
    def close_driver( self ):
        self.driver.close()
        
if __name__ == '__main__':
    chromedriver_autoinstaller.install()
    url = 'https://www.remax.pt/imoveis/venda-moradia-t3-santo-tirso-rebordoes/125651031-13'
    url = 'https://www.remax.pt/imoveis/venda-moradia-t3-santo-tirso-vila-nova-do-campo/123061225-62'
    house = Scrapper( url )
    house.print_house()
    house.close_driver()