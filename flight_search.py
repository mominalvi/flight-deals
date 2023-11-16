import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("KIWI_API_KEY")
KIWI_LOCATION_ENDPOINT = os.getenv("KIWI_LOCATION_ENDPOINT")

class FlightSearch:
    def get_iata_code(self, city_name):
        headers = {
            "apikey": API_KEY,
        }
        kiwi_params = {
            "term": city_name
        }

        iata_code = requests.get(url=KIWI_LOCATION_ENDPOINT, params=kiwi_params, headers=headers)
        return iata_code.json()['locations'][0]['code']




