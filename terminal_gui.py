
# terminal_gui.py

# Importing necessary libraries
from config import CRYPTO_CURRENCIES
from model import predict_price, create_model
from data_fetcher import fetch_data
from data_preprocessor import preprocess_data

def main():
    # Create the model
    model = create_model()

    # Fetch and preprocess the data
    crypto_data = fetch_data()
    crypto_data = preprocess_data(crypto_data)

    while True:
        # Ask the user for the crypto currency and date
        crypto = input("Enter the crypto currency: ")
        date = input("Enter the date (YYYY-MM-DD): ")

        # Predict the price
        prediction = predict_price(model, crypto_data)

        # Print the prediction
        print(f"The predicted price for {crypto} on {date} is {prediction[crypto]}")

if __name__ == "__main__":
    main()
