
# decision_maker.py

# Importing necessary libraries
from config import DECISION_THRESHOLD
from data_fetcher import fetch_data
from data_preprocessor import preprocess_data
from sklearn.model_selection import train_test_split
from model import create_model, train_model, predict_price

def make_decision():
    # Fetch the data
    crypto_data = fetch_data()

    # Preprocess the data
    preprocessed_data = preprocess_data(crypto_data)

    # Create the model
    model = create_model()

    # Dictionary to store decisions for each crypto currency
    decisions = {}

    # Loop through each crypto currency
    for crypto, (df, _) in preprocessed_data.items():
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(df.drop('future', axis=1), df['future'], test_size=0.2)

        # Train the model
        train_model(model, X_train, y_train)

        # Predict the price
        prediction = predict_price(model, {crypto: (df, _)})

        # Get the current price
        current_price = df['close'].iloc[-1]

        # If the predicted price is greater than the current price by at least the threshold, the decision is to buy
        if prediction[crypto] > current_price * (1 + DECISION_THRESHOLD):
            decisions[crypto] = 'Buy'
        else:
            decisions[crypto] = 'Hold'

    return decisions


