# Import necessary classes for managing data, flight information, notifications, and flight searches
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from flight_search import FlightSearch

# Create an instance of DataManager to handle operations related to data storage and retrieval
data_manager = DataManager()

# Create an instance of NotificationManager for handling sending of notifications
notification_manager = NotificationManager()

# Retrieve destination data such as city names and IATA codes
city_info = data_manager.get_destination_data()

# Update the IATA codes in the data storage for all destinations
data_manager.update_iata_codes(city_info)

# Apply any updates to the overall data sheet, like new or modified city information
data_manager.update_sheet()

# Create an instance of FlightData to fetch flight related information
flight_data = FlightData()

# Retrieve a list of the cheapest flights available for the destinations in city_info
data_list = flight_data.get_cheapest_flights(city_info)

# Check if the found flight prices are lower than previously recorded ones
updated_data_list = data_manager.check_if_lower(data_list)

# Send notifications with updated flight information if there are any changes in prices
notification_manager.send_messages(updated_data_list)
