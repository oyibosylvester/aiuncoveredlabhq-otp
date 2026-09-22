from twilio.rest import Client

import os

from dotenv import load_dotenv

load_dotenv()

client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))

service_sid = os.getenv("VERIFY_SERVICE_SID")

phone = input("Enter phone number: ")

print(f"Sending to {phone}...")

v = client.verify.v2.services(service_sid).verifications.create(to=phone, channel='sms')

print(f"Sent! Status: {v.status}")

code = input("Enter code from phone: ")

check = client.verify.v2.services(service_sid).verification_checks.create(to=phone, code=code)

print(f"Result: {check.status}")

print("DONE")
