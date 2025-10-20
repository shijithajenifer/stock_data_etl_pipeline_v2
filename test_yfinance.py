import yfinance as yf

print("yfinance imported successfully!")

# Test fetching a single stock
stock = yf.Ticker("RELIANCE.NS")
data = stock.history(period="1d", interval="1d")
print(data.head())
