#MARKETSTACK_KEY

#0 explore marketstack docs and find relevent url
#1 integrate API

#imports
import os #to access env variable
import requests # to call marketstack API
import json

API_KEY = os.environ.get("MARKETSTACK_KEY")
BASE_URL = 'http://api.marketstack.com/v1/'


def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY
    }
    end_point = ''.join([BASE_URL, "tickers/" , stock_symbol, "/intraday/latest"])
    api_result = requests.get(end_point, params)
    #print(api_result)
    json_result = json.loads(api_result.text)
    #print(json_result)
    return {
        "last_price": json_result["open"]
    }