import os
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
SHEETY_END = config["SHEETY_ENDPOINT"]
SHEETY_AUTH = config["SHEETY_AUTH_TOKEN"]

class DataManager:
    def __init__(self, city: str, iata_code: str, price: int) -> None:
        self.header = {
            "Authorization": f"Bearer {SHEETY_AUTH}"
        }


        self.get_response = requests.get(url=f"{SHEETY_END}?filter[city]={city}", headers=self.header)
        self.data = self.get_response.json()
        
        self.current_price = int(self.data["prices"][0]["lowestPrice"])
        self.location_row_id = self.data["prices"][0]["id"]

        self.lowest_price = 0
        if price < self.current_price:
            self.lowest_price = price
        else:
            self.lowest_price = self.current_price

        self.update_params = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": self.lowest_price,
            }
        }

        self.update_response = requests.put(url=f"{SHEETY_END}/{self.location_row_id}", headers=self.header, json=self.update_params)
        pass
    #This class is responsible for talking to the Google Sheet.
    