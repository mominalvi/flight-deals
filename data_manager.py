import os
import requests
from datetime import datetime
from flight_search import FlightSearch
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the endpoint URL for Sheety API from the environment variables
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")

class DataManager:
    def __init__(self):
        # Fetch destination data and initialize FlightSearch upon creating an instance of DataManager
        self.destination_data = self.get_destination_data()
        self.flight_search = FlightSearch()

    def get_destination_data(self):
        # Make a GET request to the Sheety API to fetch the destination data
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()

        # Store the "prices" part of the response in destination_data
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata_codes(self, city_info):
        # Update IATA codes for each city in the city_info
        for city in city_info:
            city['iataCode'] = self.flight_search.get_iata_code(city['city'])

    def update_sheet(self):
        # Update the Sheety data sheet with the new or modified city information
        for city in self.destination_data:
            sheety_params = {
                "price": {
                    "city": city['city'],
                    "iataCode": city['iataCode'],
                    "lowestPrice": city["lowestPrice"]
                }
            }
            requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=sheety_params)

    def check_if_lower(self, data_list):
        # Check if the found flight prices are lower than the recorded prices
        for dest in self.destination_data:
            for data in data_list:
                iata_code_from_data_list = data.get('cityCodeFrom') or data.get('flyFrom')
                if dest['iataCode'] == iata_code_from_data_list:
                    if data['price'] < dest['lowestPrice']:
                        dest['lowestPrice'] = data['price']

                        # Augmenting the existing dictionary with additional fields
                        dest['departureIATACode'] = data.get('flyFrom')
                        dest['destinationIATACode'] = data.get('flyTo')
                        dest['departureCity'] = data.get('cityFrom')
                        dest['destinationCity'] = data.get('cityTo')
                        dest['flightPrice'] = data.get('price')
                        dest['departureDate'] = data.get('local_departure')
                        dest['arrivalDate'] = data.get('local_arrival')

                        # Convert date format to only show YYYY-MM-DD
                        departure_date = datetime.strptime(data.get('local_departure'),'%Y-%m-%dT%H:%M:%S.%fZ').date()
                        arrival_date = datetime.strptime(data.get('local_arrival'),'%Y-%m-%dT%H:%M:%S.%fZ').date()

                        dest['departureDate'] = str(departure_date)
                        dest['arrivalDate'] = str(arrival_date)
                        break  # Exit the inner loop once a match is found

        return self.destination_data

    def update_user_sheet(self, first_name, last_name, user_email):
        # Update the user data sheet with new user information
        user_params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": user_email
            }
        }
        response = requests.post(url=SHEETY_USER_ENDPOINT, json=user_params)
        print(response.text)
