from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
import os


def send_sms(offers, to_phone_number):
    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')
    client = Client(str(account_sid), str(auth_token))

    for offer in offers:
        message = f"Oferta: {offer['title']} \n Cena: {offer['price']} \n Link: {offer['link']}"
        try:
            client.messages.create(
                body=message,
                from_=str(twilio_number),
                to=to_phone_number
            )
        except TwilioRestException as err:
            print(err)
