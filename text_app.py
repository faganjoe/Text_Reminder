import twilio
from twilio.rest import Client
import schedule
import time

phone_number = "+17152276481"
my_number = input("Number: ")


def reminder():
    account_sid = 'AC48ea0c13a4203d0614f3162db7c62d04'
    auth_token = "0eae903a3f4f792eea6f485d051c91de"
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=my_number,
        from_=phone_number,
        body="Drink Water")


schedule.every().hour.do(reminder)
