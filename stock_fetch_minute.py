import yfinance as yf
import sqlite3

# Connect to database
conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

# Choose ticker
ticker = "RELIANCE.NS"

# Fetch last 1 day, 1-minute interval
data = yf.download(tickers=ticker, period="1d", interval="1m")

# Insert into database
for time, row in data.iterrows():
    open_price = float(row["Open"])
    high_price = float(row["High"])
    low_price = float(row["Low"])
    close_price = float(row["Close"])
    volume = int(row["Volume"])
    
    cursor.execute("""
    INSERT INTO stock_prices (timestamp, ticker, open, high, low, close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (time.strftime("%Y-%m-%d %H:%M:%S"), ticker, open_price, high_price, low_price, close_price, volume))

conn.commit()
conn.close()
print(f"{len(data)} rows inserted for {ticker}!")
