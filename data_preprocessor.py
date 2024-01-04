from sklearn.preprocessing import MinMaxScaler

def preprocess_data(crypto_data):
    preprocessed_data = {}
    for crypto, df in crypto_data.items():
        df = df.dropna()
        scaler = MinMaxScaler(feature_range=(0, 1), copy=True)
        df['close'] = scaler.fit_transform(df[['close']])
        df['future'] = df['close'].shift(-1)
        df = df.dropna()
        preprocessed_data[crypto] = (df, scaler)

    return preprocessed_data
