import africastalking
import os


username = os.getenv('AFRICASTALKING_USERNAME')
api_key = os.getenv('AFRICASTALKING_API_KEY')

africastalking.initialize(
    username= username,
    api_key  = api_key
)
print(username)
print(api_key)

class send_sms():
    def send(self, phone_number, otp):
        sms = africastalking.SMS
        recipients = [phone_number]
        message = f"Your OTP is: {otp}"
        # sender = "XXYYZZ"  # Replace with your desired sender ID or short code
        print(sms, recipients, message)

        try:
            response = sms.send(message, recipients)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')
