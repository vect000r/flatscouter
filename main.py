from request import *
from parser import *


def main():
    get_offers("rzeszow", 30, 40, 350000, 500000)
    with open('offers.json', 'r') as f:
        offers = json.load(f)

        print(parse_offers(offers, 350000, 500000, 30, 40))


if __name__ == '__main__':
    main()
