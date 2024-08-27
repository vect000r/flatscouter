from request import *
from sms import *


def main():
    get_offers("rzeszow", 30, 40, 350000, 500000)
    with open('offers.json', 'r') as f:
        try:
            offers = json.load(f)
        except ValueError as err:
            print(err)

        phone_number = os.environ.get('PHONE_NUMBER')
        print(f'Found {len(offers)} offers: \n{parse_offers(offers)}')

        if input("Do you want to send the offers? (y/n) ").lower() == 'y':
            print("Sending offers")
            send_sms(offers, str(phone_number))


if __name__ == '__main__':
    main()
