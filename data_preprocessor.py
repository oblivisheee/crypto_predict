
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(crypto_data):
    preprocessed_data = {}
    for crypto, df in crypto_data.items():
        df = df.dropna()
        scaler = MinMaxScaler()
        df['close'] = scaler.fit_transform(df[['close']])
        df['future'] = df['close'].shift(-1)
        df = df.iloc[:-1]
        preprocessed_data[crypto] = (df, scaler)

    return preprocessed_data
