
# data_fetcher.py

# Importing necessary libraries
import requests
import pandas as pd
from config import API_KEY, BASE_URL, CRYPTO_CURRENCIES, HISTORICAL_DATA_PERIOD

def fetch_data():
    # Dictionary to store data for each crypto currency
    crypto_data = {}

    # Loop through each crypto currency
    for crypto in CRYPTO_CURRENCIES:
        # URL to fetch historical data
        url = f"{BASE_URL}/v1/cryptocurrency/quotes/historical?symbol={crypto}&interval={HISTORICAL_DATA_PERIOD}&apikey={API_KEY}"

        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()

            # Convert the data to a pandas DataFrame
            df = pd.DataFrame(data['data']['quote'])

            # Set the date as the index
            df.set_index('timestamp', inplace=True)

            # Store the DataFrame in the dictionary
            crypto_data[crypto] = df
        else:
            print(f"Failed to fetch data for {crypto}. Status code: {response.status_code}")

    return crypto_data

