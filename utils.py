import os
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib
import tensorflow as tf

# Directory to store models and scalers
MODELS_DIR = "models"
os.makedirs(MODELS_DIR, exist_ok=True)

# Fetch historical stock data from Yahoo Finance
def fetch_stock_data(symbol, start="2015-01-01", end="2024-12-31"):
    df = yf.download(symbol, start=start, end=end)
    if df.empty or "Close" not in df:
        raise ValueError(f"No data found for {symbol}")
    return df["Close"].values.reshape(-1, 1)

# Train LSTM model and save model + scaler
def train_and_save_model(symbol, prices):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(prices)

    X, y = [], []
    for i in range(10, len(scaled)):
        X.append(scaled[i - 10:i])
        y.append(scaled[i])

    X, y = np.array(X), np.array(y)

    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(10, 1)),
        LSTM(50),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=20, batch_size=32, verbose=0)

    # Save model and scaler
    model.save(f"{MODELS_DIR}/{symbol}_model.h5")
    joblib.dump(scaler, f"{MODELS_DIR}/{symbol}_scaler.save")

# Load model and scaler; if not exist, fetch data and train
def load_model_and_scaler(symbol):
    model_path = f"{MODELS_DIR}/{symbol}_model.h5"
    scaler_path = f"{MODELS_DIR}/{symbol}_scaler.save"

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        prices = fetch_stock_data(symbol)
        train_and_save_model(symbol, prices)

    model = tf.keras.models.load_model(model_path, compile=False)
    scaler = joblib.load(scaler_path)
    return model, scaler
