#Precio del Bitcoin

import requests

response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')


price = response.json()['data']['amount']

print(f"El precio actual de Bitcoin es {price} USD")
