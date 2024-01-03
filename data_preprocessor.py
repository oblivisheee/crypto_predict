
# data_preprocessor.py

# Importing necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(crypto_data):
    # Dictionary to store preprocessed data for each crypto currency
    preprocessed_data = {}

    # Loop through each crypto currency
    for crypto, df in crypto_data.items():
        # Drop any rows with missing values
        df.dropna(inplace=True)

        # Create a MinMaxScaler
        scaler = MinMaxScaler()

        # Scale the 'close' column to be between 0 and 1
        df['close'] = scaler.fit_transform(df[['close']])

        # Add a 'future' column that is the 'close' column shifted up 1
        df['future'] = df['close'].shift(-1)

        # Drop the last row, which now has a missing 'future' value
        df.drop(df.tail(1).index, inplace=True)

        # Store the DataFrame and the scaler in the dictionary
        preprocessed_data[crypto] = (df, scaler)

    return preprocessed_data

