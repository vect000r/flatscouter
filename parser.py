def parse_offers(offers, min_price, max_price, min_area, max_area):
    parsed_offers = []

    for offer in offers:
        price = int(''.join(filter(str.isdigit, offer['price'])))
        area = float(''.join(filter(lambda x: x.isdigit() or x == '.', offer['area'])))

        if min_price <= price <= max_price and min_area <= area <= max_area:
            parsed_offers.append(offer)

    return parsed_offers
