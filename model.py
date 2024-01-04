
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, ReLU
from tensorflow.keras.layers import MultiHeadAttention, LayerNormalization
from tensorflow.keras.callbacks import EarlyStopping

def create_model():
    inputs = Input(shape=(None, 1))
    x = MultiHeadAttention(num_heads=2, key_dim=2)(inputs, inputs)
    x = Dropout(0.2)(x)
    x = LayerNormalization(epsilon=1e-6)(x)
    x = Dense(1)(x)
    outputs = ReLU()(x)
    model = Model(inputs=inputs, outputs=outputs)
    model.compile(loss='mse', optimizer='adam')
    return model

def train_model(model, X_train, y_train, scaler):
    X_train = scaler.transform(X_train.reshape(-1, 1))
    y_train = scaler.transform(y_train.reshape(-1, 1))
    early_stopping = EarlyStopping(monitor='val_loss', patience=3)
    history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping])
    print(history.history)
    return model

def predict_price(model, crypto_data, date=None):
    predictions = {}
    for crypto, (df, scaler) in crypto_data.items():
        if date:
            df = df[df.index <= date]
        last_60_days = df['close'][-60:].values.reshape(-1, 1)
        last_60_days_scaled = scaler.transform(last_60_days)
        last_60_days_scaled = last_60_days_scaled.reshape((1, last_60_days_scaled.shape[0], 1))
        prediction = model.predict(last_60_days_scaled)
        if prediction[0, 0] <= 0:
            print(f"Warning: Prediction for {crypto} is less than or equal to zero. Please check the model or data.")
            predictions[crypto] = 0
        else:
            predictions[crypto] = scaler.inverse_transform(prediction)[0, 0]
    return predictions
