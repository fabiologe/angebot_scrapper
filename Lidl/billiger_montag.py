import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://www.lidl.de/c/billiger-montag/a10006065?channel=store&tabCode=Current_Sales_Week#10073296'

def get_bm_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup.find('div', class_= 'm-price__price m-price__price--small'))
    product_elements = soup.find_all('li', class_='ACampaignGrid__item ACampaignGrid__item--product')

    products_data = []
    

    for product in product_elements:
        title_elem = product.find('div', attrs={'fulltitle': True})
        title = title_elem['fulltitle'] if title_elem else 'Unknown Title'
        price = product.find('div', class_= 'price')
        
        
        products_data.append({'title': title, 'price': price})

    return products_data

product_data = get_bm_data(url)

for product in product_data:
    print(f"Product: {product['title']}, Price: {product['price']}")
