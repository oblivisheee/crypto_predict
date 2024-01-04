
from model import predict_price, create_model
from data_fetcher import fetch_data
from data_preprocessor import preprocess_data

def main():
    model = create_model()

    crypto = input("Enter the crypto currency: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    return_times = input("Enter quantity of fetch repeatings: ")

    crypto_data = fetch_data(coin=crypto, return_times=return_times)
    crypto_data = preprocess_data(crypto_data)

    prediction = predict_price(model, crypto_data, date=date)
    print(f"The predicted price for {crypto} on {date} is {prediction[crypto]}")

if __name__ == "__main__":
    main()

