import yfinance as yf
import pandas as pd
import time
import os

# Create folder if not exists
if not os.path.exists("raw_data"):
    os.makedirs("raw_data")

tickers = ["AAPL", "GOOG", "MSFT"]

for ticker in tickers:
    print(f"Fetching data for {ticker}...")
    data = yf.download(tickers=ticker, period="1d", interval="1m")
    filename = f"raw_data/{ticker}_{time.strftime('%Y%m%d_%H%M%S')}.csv"
    data.to_csv(filename)
    print(f"✅ Saved: {filename}")

print("\nAll data successfully saved in 'raw_data' folder.")
