import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

# Load Twilio credentials from environment variables
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    sender_number = request.values.get("From", "")

    resp = MessagingResponse()
    msg = resp.message()

    # Responding based on user message
    if "hello" in incoming_msg:
        msg.body("Hi there! How can I assist you? 😊")
    elif "help" in incoming_msg:
        msg.body("You can ask me anything, like 'Hello' or 'What can you do?'.")
    else:
        msg.body("I'm sorry, I didn't understand that.")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
