import yfinance as yf
import pandas as pd

# 📌 Step 1: Configuration
ticker = "005930.KS"  # Change this to your desired stock symbol (e.g., 'GOOGL', 'TSLA', 'RELIANCE.NS')
start_date = "2020-01-01"
end_date = "2024-12-31"

# 📌 Step 2: Download historical stock data
data = yf.download(ticker, start=start_date, end=end_date)

# 📌 Step 3: Clean and format the DataFrame
df = data[["Close"]].reset_index()
df.columns = ["date", "close"]

# 📌 Step 4: Save to CSV
csv_filename = f"{ticker}_prices.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ Stock data saved to: {csv_filename}")
