from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env
app = Flask(__name__) 

ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN =  os.environ.get("TWILIO_TOKEN")
client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

def process_msg(msg):
    response = ""
    if msg == "hi":
        response = "Hello, welcome to the stock market Bot!"
        response += "Please type sym:<stock_symbol> to know the (open) price of the stock."
    elif 'sym:' in msg:
        data = msg.split(":") #split msg after : to get stock code
        stock_symbol = data[1] #1 element is stock_symbol, 0 element is sym
        stock_price = get_stock_price(stock_symbol)
        last_price = stock_price['last_price']
        last_price_str = str(last_price) #convert last_price from float to string
        response = "The stock price of " + stock_symbol + "is : $" + last_price_str
    else:
        response = "Please type hi to get started"
    return response

#get the data from flask using POST methods
@app.route("/webhook", methods=["POST"])
def webhook():
    f = request.form
    msg = f["Body"]
    sender = f["From"]
    response = process_msg(msg)
    send_msg(response, sender)
    return "OK", 200

    #Steps
    #0 get account id and token from twilio and set in env
    #TWILIO_ACCOUNT & TWILIO_TOKEN

    #1 import CLIENT from twilio
    #2 initialize client

    #3 write a function to process msg
    #4 write a function to send message
    #5 generate a response
    #6 check response in whatsapp

    
    