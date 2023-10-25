
import telnyx

telnyx.api_key = "KEY018B4BD73F3FD1212EA236992F3E2279_qM2HBs1Mnep23FbTEpLt0v"

your_telnyx_number = "+917385299597"
destination_number = "+918263804860"

telnyx.Message.create(
    from_=your_telnyx_number,
    to=destination_number,
    text="Demo SMS Kam krta hia ya nhi wo dekh raha hoo",
)

import telnyx

# Replace with your Telnyx API credentials
api_key = 'KEY018B4BD73F3FD1212EA236992F3E2279_qM2HBs1Mnep23FbTEpLt0v'
api_secret = 'DH0Ub1zaOXKiBMREo1RkRLNzs32RqJtckpcGSfMsLFM='

# Initialize the Telnyx API client
telnyx.api_key = (api_key, api_secret)

# Define the message parameters
message = {
    'from': 'YOUR_PHONE_NUMBER',  # Use one of your Telnyx phone numbers
    'to': '+1234567890',  # The recipient's phone number
    'text': 'Hello from Telnyx!',  # The message text
}

try:
    # Send the SMS
    response = telnyx.Message.create(**message)
    print("Message sent successfully with ID:", response.id)
except telnyx.error.TelnyxError as e:
    print("Error:", e)
