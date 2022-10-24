import requests
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values(".env")
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com"
SEARCH_API_KEY = config["TEQUILA_API"]


class FlightSearch:
    def __init__(self) -> None:
        self.header = {
            "apikey": SEARCH_API_KEY,
            "Content-Encoding": "gzip"
        }
        self.today = datetime.now()
        self.tomorrow = self.today + datetime.timedelta(day= 1)
        self.months_6_away = self.today + datetime.timedelta(day= 6 * 30)

    def find_iata(self, city: str):
        self.find_iata_params = {
            "term": city,
            "location_types": "city",
        }

        self.find_iata_response = requests.get(
            url=f"{SEARCH_ENDPOINT}/locations/query", headers=self.header, params=self.find_iata_params)
        self.find_iata_response.raise_for_status()
        self.iata_data = self.find_iata_response.json()
        self.code = self.iata_data["locations"][0]["code"]
        return self.code


    def search_flights(self, departing, destination, currency, minimum_stay, maximum_stay):
        self.search_flights_params = {
            "fly_from": departing,
            "fly_to": destination,
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.months_6_away.strftime("%d/%m/%Y"),
            "curr": currency,
            "nights_in_dst_from": minimum_stay,
            "nights_in_dst_to": maximum_stay,
            "flight_type": "round"
        }

    # This class is responsible for talking to the Flight Search API.
