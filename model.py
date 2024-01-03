
# model.py

# Importing necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

def create_model():
    # Create a Sequential model
    model = Sequential()

    # Add an LSTM layer with 50 units
    model.add(LSTM(50, return_sequences=True, input_shape=(None, 1)))

    # Add a Dropout layer with a dropout rate of 0.2
    model.add(Dropout(0.2))

    # Add another LSTM layer with 50 units
    model.add(LSTM(50, return_sequences=False))

    # Add a Dropout layer with a dropout rate of 0.2
    model.add(Dropout(0.2))

    # Add a Dense layer with 1 unit
    model.add(Dense(1))

    # Compile the model with mean squared error loss and the Adam optimizer
    model.compile(loss='mse', optimizer='adam')

    return model

def train_model(model, X_train, y_train):
    # Create an EarlyStopping callback that stops training when the validation loss stops improving
    early_stopping = EarlyStopping(monitor='val_loss', patience=3)

    # Train the model for 100 epochs with a batch size of 32 and use 20% of the data for validation
    history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

    # Print the training process
    print("Training process:")
    print(history.history)

def predict_price(model, crypto_data):
    # Dictionary to store predictions for each crypto currency
    predictions = {}

    # Loop through each crypto currency
    for crypto, (df, scaler) in crypto_data.items():
        # Get the last 60 days of closing prices and scale them
        last_60_days = scaler.transform(df['close'][-60:].values.reshape(-1, 1))

        # Reshape the data to be 3-dimensional
        last_60_days = last_60_days.reshape((1, last_60_days.shape[0], 1))

        # Predict the price
        prediction = model.predict(last_60_days)

        # Rescale the prediction back to the original scale
        prediction = scaler.inverse_transform(prediction)

        # Store the prediction in the dictionary
        predictions[crypto] = prediction[0][0]

    return predictions
