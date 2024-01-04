import ccxt
import pandas as pd
from datetime import datetime, timedelta
from config import  HISTORICAL_DATA_PERIOD
from tqdm import tqdm

def fetch_data(coin: str, return_times: int=100):
    crypto_data = {}

    exchange = ccxt.binance({
        'options': {
            'defaultType': 'future'
        }
    })
    coins = [coin]
    for crypto in coins:
        for i in tqdm(range(return_times), desc="Fetching data"):
            end_date = datetime.now() - timedelta(days=i*30)
            start_date = end_date - timedelta(days=30)

            try:
                data = exchange.fetch_ohlcv(crypto+'/USDT', HISTORICAL_DATA_PERIOD, 
                                            since=int(start_date.timestamp() * 1000), 
                                            limit=1000)
                if not data:
                    raise ValueError(f"No data returned from exchange for {crypto}")

                df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

                df.set_index('timestamp', inplace=True)

                if crypto in crypto_data:
                    crypto_data[crypto] = pd.concat([crypto_data[crypto], df])
                else:
                    crypto_data[crypto] = df

            except (ccxt.NetworkError, ccxt.ExchangeError, ccxt.BaseError, ValueError) as e:
                print(f"Error occurred while fetching data for {crypto}: {e}")
                continue
    return crypto_data
