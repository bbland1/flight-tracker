from twilio.rest import Client
from dotenv import dotenv_values

config = dotenv_values(".env")
TWILIO_SID = config["TWILIO_SID"]
TWILIO_AUTH_TOKEN = config["TWILIO_AUTH"]
TWILIO_VIRTUAL_NUMBER = config["TWILIO_VIRTUAL_NUM"]
TWILIO_VERIFIED_NUMBER = config["TWILIO_REAL_NUM"]
class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_text(self, message):
        self.message = self.client.messages.create(
            body = message,
            from_ = TWILIO_VIRTUAL_NUMBER,
            to = TWILIO_VERIFIED_NUMBER
        )

        # when message sending works print this
        print(self.message.sid)
    #This class is responsible for sending notifications with the deal flight details.