import requests
import time

# Coinbase API endpoint URL for Bitcoin price
url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

# Set API key and secret
api_key = 'tj00lqyVBVMnElDe'
api_secret = 'RhGBXyDBWcvmDlAkjJif4pkNSqTJhyqp'

# Define function to get current Bitcoin price
def get_btc_price():
    response = requests.get(url, auth=(api_key, api_secret))
    if response.status_code == 200:
        data = response.json()
        return float(data['data']['amount'])
    else:
        return None

# Continuously update Bitcoin price every 10 seconds
while True:
    price = get_btc_price()
    if price is not None:
        print(f'Bitcoin price: {price:.2f} USD')
    else:
        print('Error getting Bitcoin price')
    time.sleep(10)
