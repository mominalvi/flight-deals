import os
import requests
import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the Kiwi API endpoint and API key from environment variables
KIWI_DATE_ENDPOINT = os.getenv("KIWI_DATE_ENDPOINT")
API_KEY = os.getenv("KIWI_API_KEY")

class FlightData:
    def __init__(self):
        # Initialize with a default price value
        self.price = 0

    def get_cheapest_flights(self, city_info):
        # Get the cheapest flight for each city in the city_info list
        return [self.get_cheapest_flight(city['iataCode']) for city in city_info]

    def get_cheapest_flight(self, city_iata):
        # Set headers for the API request with the API key
        headers = {
            "apikey": API_KEY
        }

        # Calculate dates for 'tomorrow' and 'six months from tomorrow'
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        formatted_tmrw = tomorrow.date().strftime("%d/%m/%Y")
        six_months = tomorrow + relativedelta(months=+6)
        formatted_six = six_months.date().strftime("%d/%m/%Y")

        # Set parameters for the API request including from location and date range
        kiwi_params = {
            "fly_from": city_iata,
            "date_from": formatted_tmrw,
            "date_to": formatted_six,
            "curr": "GBP"
        }

        # Make the API request to the Kiwi API
        responses = requests.get(url=KIWI_DATE_ENDPOINT, params=kiwi_params, headers=headers)
        try:
            # Attempt to parse the JSON response and return the first flight data
            data = responses.json()
            return data['data'][0]
        except IndexError:
            # Handle the case where no flights are found
            print(f"No flights found for {city_iata}.")
            return None
