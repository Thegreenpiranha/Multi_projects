import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Coinbase API endpoint URL for Bitcoin price
url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

# Set API key and secret
api_key = 'tj00lqyVBVMnElDe'
api_secret = 'RhGBXyDBWcvmDlAkjJif4pkNSqTJhyqp'

# Set time range for historical data
start_time = datetime.now() - timedelta(days=7)
end_time = datetime.now()

# Format time range for Coinbase API request
start_time_str = start_time.isoformat()
end_time_str = end_time.isoformat()

# Coinbase API endpoint URL for historical Bitcoin prices
historical_url = f'https://api.coinbase.com/v2/prices/BTC-USD/spot?start={start_time_str}&end={end_time_str}'

# Create empty lists for timestamp and price data
timestamps = []
prices = []

# Loop through historical data and append to lists
response = requests.get(historical_url, auth=(api_key, api_secret))
if response.status_code == 200:
    data = json.loads(response.text)
    for item in data['data']:
        timestamp = datetime.fromisoformat(item['time'].replace('Z', '+00:00'))
        price = float(item['price'])
        timestamps.append(timestamp)
        prices.append(price)

# Create graph of Bitcoin prices over time
plt.plot(timestamps, prices)
plt.title('Bitcoin Prices Over Time')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.show()
