import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

# Load data
df = pd.read_csv("stock_prices.csv")  # Must contain a 'close' column
prices = df["close"].values.reshape(-1, 1)

# Scale prices
scaler = MinMaxScaler()
scaled_prices = scaler.fit_transform(prices)
joblib.dump(scaler, "scaler.save")

# Create sequences
X, y = [], []
sequence_length = 10
for i in range(sequence_length, len(scaled_prices)):
    X.append(scaled_prices[i-sequence_length:i])
    y.append(scaled_prices[i])

X, y = np.array(X), np.array(y)

# Define LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
    LSTM(50),
    Dense(1)
])

# Compile & train
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X, y, epochs=20, batch_size=32)

# Save model
model.save("stock_model.h5")
print("✅ Model trained and saved.")
