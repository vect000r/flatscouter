import json
import requests
from bs4 import BeautifulSoup


def get_offers(location, min_area, max_area, min_price, max_price):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = f"https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/podkarpackie/rzeszow/rzeszow/{location}?priceMin={min_price}&priceMax={max_price}&areaMin={min_area}&areaMax={max_area}&daysSinceCreated=1&by=DEAFULT&direction=DESC&viewType=listing"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('Error requesting data from otodom.pl')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    offers = []

    for offer in soup.find_all('div', class_='css-13gthep'):
        try:
            price = offer.find('span', class_='css-2bt9f1').text.strip()
            title = offer.find('p', class_='css-u3orbr').text.strip()
            location = offer.find('p', class_='css-42r2ms').text.strip()
            rooms = offer.find('dd').text.strip()
            link = offer.find('a', class_='css-16vl3c1')['href']
            link = f"https://www.otodom.pl{link}"

            offers.append({
                'price': price,
                'title': title,
                'location': location,
                'rooms': rooms,
                'link': link
            })

        except AttributeError as e:
            print(f"Error while parsing the offer: {e}")

    with open('offers.json', 'w', encoding='utf-8') as f:
        json.dump(offers, f, ensure_ascii=False, indent=4)


def parse_offers(offers):
    parsed_offers = []

    if len(offers) != 0:
        for offer in offers:
            parsed_offers.append(offer['link'])
        return parsed_offers

    return 'No offers to show'
