import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

    def send_messages(self, updated_data_list):
        for city in updated_data_list:
            self.send_message(city)

    def send_message(self, city_info):
        proxy_client = TwilioHttpClient()
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN, http_client=proxy_client)
        message = client.messages.create(
            body=f"Low price alert! Only £{city_info['lowestPrice']} to fly"
                 f" from {city_info['departureCity']}-{city_info['departureIATACode']}"
                 f" to {city_info['destinationCity']}-{city_info['destinationIATACode']}"
                 f" from {city_info['departureDate']} to {city_info['arrivalDate']}",
            from_='+19388887294',
            to='+16475078485',
        )
        print(message.status)
