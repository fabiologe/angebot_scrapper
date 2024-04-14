import requests
from bs4 import BeautifulSoup
import json

def edeka_Top4(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    # Find all product boxes
    product_boxes = soup.find_all('div', class_='produkt_box')

    for product_box in product_boxes:
        # Find product name
        product_name = product_box.find('div', class_='beschreibung').find('b').text.strip()

        # Find product price
        product_price = product_box.find('span', style='color:#383838; font-size:14px; float:right; padding-right: 0px;text-align:right').find('b').text.strip()

        products.append({"name": product_name, "price": product_price})

    # Convert list of products to JSON
    json_data = json.dumps(products, ensure_ascii=False, indent=2)

    # Print or save JSON data
    print(json_data)

    # If you want to save it to a file
    with open('edekaTop4.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

    return json_data

def generate_edeka_url(postal_code):
    base_url = "https://www.aktionspreis.de/prospekt/edeka-angebote"
    url = f"{base_url}?plz={postal_code}"
    return url

postal_code = 66113
url_post = generate_edeka_url(postal_code)
edeka_Top4(url_post)
