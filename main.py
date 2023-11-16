from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from flight_search import FlightSearch

data_manager = DataManager()
notification_manager = NotificationManager()

city_info = data_manager.get_destination_data()
data_manager.update_iata_codes(city_info)
data_manager.update_sheet()

flight_data = FlightData()
data_list = flight_data.get_cheapest_flights(city_info)

updated_data_list = data_manager.check_if_lower(data_list)

notification_manager.send_messages(updated_data_list)
