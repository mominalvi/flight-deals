import os
import requests
import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
load_dotenv()

KIWI_DATE_ENDPOINT = os.getenv("KIWI_DATE_ENDPOINT")
API_KEY = os.getenv("KIWI_API_KEY")

class FlightData:
    def __init__(self):
        self.price = 0

    def get_cheapest_flights(self, city_info):
        return [self.get_cheapest_flight(city['iataCode']) for city in city_info]

    def get_cheapest_flight(self, city_iata):
        headers = {
            "apikey": API_KEY
        }

        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        formatted_tmrw = tomorrow.date().strftime("%d/%m/%Y")
        six_months = tomorrow + relativedelta(months=+6)
        formatted_six = six_months.date().strftime("%d/%m/%Y")

        kiwi_params = {
            "fly_from": city_iata,
            "date_from": formatted_tmrw,
            "date_to": formatted_six,
            "curr": "GBP"
        }

        responses = requests.get(url=KIWI_DATE_ENDPOINT, params=kiwi_params, headers=headers)
        try:
            data = responses.json()
            return data['data'][0]
        except IndexError:
            print(f"No flights found for {city_iata}.")
            return None
