import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com"
SEARCH_API_KEY = config["TEQUILA_API"]

class FlightSearch:
    def __init__(self) -> None:
        self.header = {
            "apikey": SEARCH_API_KEY,
            "Content-Encoding": "gzip"
        }

    def find_iata(self, city: str):
        self.find_iata_params = {
            "term": city,
            "location_types": "city",
        }

        self.find_iata_response = requests.get(url=f"{SEARCH_ENDPOINT}/locations/query", headers=self.header, params=self.find_iata_params)
        self.find_iata_response.raise_for_status()
        self.iata_data = self.find_iata_response.json()
        self.code = self.iata_data["locations"][0]["code"]
        return self.code

    
    #This class is responsible for talking to the Flight Search API.