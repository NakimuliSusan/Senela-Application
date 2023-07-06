from django.conf import settings
from twilio.rest import Client
import random


class MessageHandler:
    phone_number = None
    otp = None

    def __init__(self,phone_number, otp):
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_phone (self):

        client = Client(settings.account_sid, settings.auth_token)
        message = client.messages.create(
            body = f"Your otp is {self.otp }"
        )
