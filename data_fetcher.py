
# data_fetcher.py

# Importing necessary libraries
import ccxt
import pandas as pd
from config import CRYPTO_CURRENCIES, HISTORICAL_DATA_PERIOD

def fetch_data():
    # Dictionary to store data for each crypto currency
    crypto_data = {}

    # Initialize the ccxt library
    exchange = ccxt.binance()

    # Loop through each crypto currency
    for crypto in CRYPTO_CURRENCIES:
        # Fetch historical data
        # Increase the timeframe to fetch maximum historical data for better training
        data = exchange.fetch_ohlcv(crypto+'/USDT', HISTORICAL_DATA_PERIOD, since=0) 

        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

        # Convert the timestamp to a datetime object
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Set the date as the index
        df.set_index('timestamp', inplace=True)

        # Store the DataFrame in the dictionary
        crypto_data[crypto] = df

    return crypto_data

