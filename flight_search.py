import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key and location endpoint from the Kiwi API stored in environment variables
API_KEY = os.getenv("KIWI_API_KEY")
KIWI_LOCATION_ENDPOINT = os.getenv("KIWI_LOCATION_ENDPOINT")

class FlightSearch:
    def get_iata_code(self, city_name):
        # Set headers for the API request with the API key
        headers = {
            "apikey": API_KEY,
        }

        # Prepare parameters for the API request with the city name
        kiwi_params = {
            "term": city_name
        }

        # Make a GET request to the Kiwi API to retrieve the IATA code for the given city
        iata_code = requests.get(url=KIWI_LOCATION_ENDPOINT, params=kiwi_params, headers=headers)

        # Return the IATA code from the JSON response
        return iata_code.json()['locations'][0]['code']
