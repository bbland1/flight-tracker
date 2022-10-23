import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com"
SEARCH_API_KEY = config["TEQUILA_API"]


class FlightData:
    def __init__(self) -> None:
        self.header = {
            "apikey": SEARCH_API_KEY,
            "Content-Encoding": "gzip"
        }
    #This class is responsible for structuring the flight data.
    