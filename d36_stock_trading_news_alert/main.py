
import requests
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

KEY = "XTW7H3LP76PJET4L"
FUNCTION = "TIME_SERIES_DAILY"
SYMBOL = "TSLA"
INTERVAL = "5miny"

URL = "https://www.alphavantage.co/query"
parameters = {
    "function":FUNCTION,
    "symbol":SYMBOL,
    "interval":INTERVAL,
    "apikey":KEY
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()

with open("./stock_data.json", mode="w") as stock_file:
    json.dump(data, stock_file, indent=4)

print(data)



