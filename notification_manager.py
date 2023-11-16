import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class NotificationManager:
    # Retrieve Twilio account credentials from environment variables
    ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

    def send_messages(self, updated_data_list):
        # Iterate over each city in the updated data list and send a message
        for city in updated_data_list:
            self.send_message(city)

    def send_message(self, city_info):
        # Create a Twilio HTTP client for sending messages
        proxy_client = TwilioHttpClient()
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN, http_client=proxy_client)

        # Compose the message body with flight details
        message = client.messages.create(
            body=f"Low price alert! Only £{city_info['lowestPrice']} to fly"
                 f" from {city_info['departureCity']}-{city_info['departureIATACode']}"
                 f" to {city_info['destinationCity']}-{city_info['destinationIATACode']}"
                 f" from {city_info['departureDate']} to {city_info['arrivalDate']}",
            from_=os.getenv('FROM_NUMBER'),  # Sender's number, fetched from environment variable
            to=os.getenv('TO_NUMBER'),  # Receiver's number, fetched from environment variable
        )

        # Print the status of the message to the console for confirmation
        print(message.status)
