from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup
origins = ["http://localhost:5173"]  # Adjust this to match your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model & scaler
model = tf.keras.models.load_model("stock_model.h5")
scaler = joblib.load("scaler.save")

# Request schema
class StockInput(BaseModel):
    prices: list  # List of last 10 closing prices

@app.get("/")
def read_root():
    return {"message": "Welcome to the Real Stock Predictor 🚀"}

@app.post("/predict")
def predict(input: StockInput):
    prices = np.array(input.prices).reshape(-1, 1)

    if len(prices) < 10:
        return {"error": "Please provide at least 10 prices!"}

    scaled = scaler.transform(prices)
    input_seq = scaled[-10:].reshape(1, 10, 1)

    prediction = model.predict(input_seq)
    predicted_price = scaler.inverse_transform(prediction)[0][0]

    return {"predicted_price": float(predicted_price)}
