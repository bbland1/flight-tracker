import requests
from dotenv import dotenv_values
from datetime import datetime

from flight_data import FlightData

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
        self.tomorrow = self.today + datetime.timedelta(day=1)
        self.months_6_away = self.today + datetime.timedelta(day=6 * 30)

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

    def search_flights(self, departing_city_code: str, destination_city_code: str, mini_stay_time: int, max_stay_time: int):
        self.search_flights_params = {
            "fly_from": departing_city_code,
            "fly_to": destination_city_code,
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.months_6_away.strftime("%d/%m/%Y"),
            "curr": "USD",
            # minimum amount of nights staying in the fly_to location
            "nights_in_dst_from": mini_stay_time,
             # maximum amount of nights staying in the fly_to location
            "nights_in_dst_to": max_stay_time,
            # every flight is round trip
            "flight_type": "round",
            # searches will return  the cheapest flights to every city covered by the fly_to parameter
            "one_for_city": 1,
            # all searches are direct flights to the location
            "max_stopovers": 0,
        }

        self.flights_response = requests.get(
            url=f"{SEARCH_ENDPOINT}/v2/search", headers=self.header, params=self.search_flights_params)

        try:
            self.data = self.flights_response.json()["data"][0]
        except IndexError:
            print(f"No flights were found for {destination_city_code}")
            return None

        # because ofo how the search is set up the results returned are specified to be able to be used with this structure of search and information
        self.flight_data = FlightData(
            price = self.data["price"],
            origin_city = self.data["route"][0]["cityFrom"],
            origin_airport = self.data["route"][0]["flyFrom"],
            destination_city = self.data["route"][0]["cityTo"],
            destination_airport = self.data["route"][0]["flyTo"],
            out_date = self.data["route"][0]["local_departure"].split("T")[0],
            return_date = self.data["route"][1]["local_departure"].split("T")[0])

    # This class is responsible for talking to the Flight Search API.
