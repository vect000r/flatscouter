import json

import requests
from bs4 import BeautifulSoup


def get_offers(location, min_area, max_area, min_price, max_price):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = f"https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/podkarpackie/rzeszow/rzeszow/{location}?priceMin={min_price}&priceMax={max_price}&areaMin={min_area}&areaMax={max_area}&viewType=listing"
    response = requests.get(url, headers=headers)
    print(response.text)
    if response.status_code != 200:
        print('Error requesting data from otodom.pl')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    with open('offers.json', 'w', encoding='utf-8') as f:
        json.dump(response.text, f, ensure_ascii=False, indent=4)

    offers = []

    for offer in soup.find_all('div', class_='offer-item-details'):
        title = offer.find('span', class_='offer-item-title').text.strip()
        price = offer.find('li', class_='offer-item-price').text.strip()
        area = offer.find('li', class_='offer-item-area').text.strip()
        link = offer.find('a', class_='offer-item-title')['href']

        offers.append({
            'title': title,
            'price': price,
            'area': area,
            'link': f"https://www.otodom.pl{link}"
        })

    #with open('offers.json', 'w', encoding='utf-8') as f:
    #    json.dump(offers, f, ensure_ascii=False, indent=4)
