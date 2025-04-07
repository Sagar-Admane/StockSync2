from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from utils import load_model_and_scaler, fetch_stock_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StockRequest(BaseModel):
    symbol: str
    prices: list = []  # Optional: you can pass live prices or use from yfinance

@app.post("/predict")
def predict(req: StockRequest):
    symbol = req.symbol.upper()

    try:
        model, scaler = load_model_and_scaler(symbol)

        if req.prices:
            prices = np.array(req.prices).reshape(-1, 1)
        else:
            prices = fetch_stock_data(symbol)[-100:]  # Use recent 100 days

        scaled = scaler.transform(prices)

        if len(scaled) < 10:
            return {"error": "Need at least 10 prices."}

        input_seq = scaled[-10:].reshape(1, 10, 1)
        prediction = model.predict(input_seq)
        predicted_price = scaler.inverse_transform(prediction)[0][0]

        return {"predicted_price": float(predicted_price)}

    except Exception as e:
        return {"error": str(e)}
