import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
SHEETY_END = config["SHEETY_ENDPOINT"]
SHEETY_AUTH = config["SHEETY_AUTH_TOKEN"]


class DataManager:
    def __init__(self) -> None:
        self.header = {
            "Authorization": f"Bearer {SHEETY_AUTH}",
            "Content-Type": "application/json"
        }

    def update_data(self, city, iata_code, price):
        try:
            self.get_response = requests.get(
                url=f"{SHEETY_END}?filter[city]={city}", headers=self.header)
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
            self.get_response = requests.put(
                url=f"{SHEETY_END}/{self.location_row_id}", headers=self.header, json=self.update_params)
        except IndexError:
            self.add_params = {
                "price": {
                    "city": city,
                    "iataCode": iata_code,
                    "lowestPrice": price,
                }
            }
            self.get_response = requests.post(
                url=SHEETY_END, headers=self.header, json=self.add_params)
        finally:
            self.get_response.raise_for_status()

    def get_all_data(self):
        self.get_all_response = requests.get(
            url=SHEETY_END, headers=self.header)
        self.all_data = self.get_all_response.json()
        return self.all_data["prices"]

    def add_iata_code(self, id, iata, city, price):
        self.iata_params = {
            "price": {
                "city": city,
                "iataCode": iata,
                "lowestPrice": price,
            }
        }

        self.add_iata_response = requests.put(
            url=f"{SHEETY_END}/{id}", headers=self.header, json=self.iata_params)
        self.add_iata_response.raise_for_status()

    # This class is responsible for talking to the Google Sheet.
