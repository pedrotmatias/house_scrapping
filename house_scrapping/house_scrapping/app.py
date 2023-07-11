import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
house = {}


url = 'https://www.remax.pt/imoveis/venda-moradia-t3-santo-tirso-rebordoes/125651031-13'
url = 'https://www.remax.pt/imoveis/venda-moradia-t3-santo-tirso-vila-nova-do-campo/123061225-62'

house['Link'] = url
driver.get( house['Link'] )

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

top_info = soup.find('div', 'listing-top-info')
for info in top_info:
    price = top_info.find( 'span', 'listing-price' )
    house['price'] = price.string.replace(" ", "").replace("€","")

for info in top_info:
    id = top_info.find( 'span', 'listing-title' )
    house['id'] = id.string.replace(" ", "").replace("€","")


remax_table = soup.find( 'div' , { 'id' : 'tabs-navigation'} )
details = remax_table.find( 'div', {'id' : 'details'} )
array_of_vals = []
for value in details.find_all( 'td', class_=lambda x: x != 'first-column' ):
    array_of_vals.append( value.text.replace(" ", "").replace("€","") )

if array_of_vals:
    house['Private Building Area'] = array_of_vals[0]
    house['Building Area'] = array_of_vals[1]
    house['Total Area'] = array_of_vals[2]
    house['Total Useful Area'] = array_of_vals[3]
    house['Number of Rooms'] = array_of_vals[4]
    house['Year of construction'] = array_of_vals[ 5 ]
    house['Floor'] = array_of_vals [6]
    house['Number of WCs'] = array_of_vals [7]
    house['Elevator'] = array_of_vals [8]
    house['Parking'] = array_of_vals [9]

for items in house.items():
    print( items)