from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

google_data = DataManager()
flight_search = FlightSearch()

sheets_data = google_data.get_all_data()

for place in sheets_data:
    if place["iataCode"] == "":
        google_data.add_iata_code(place["id"], flight_search.find_iata(
            place["city"]), place["city"], place["lowestPrice"])
