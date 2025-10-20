import sqlite3
import pandas as pd
import streamlit as st

st.title("📈 Stock Price Dashboard")

# Connect to the SQLite database
conn = sqlite3.connect("stocks.db")

# Dropdown for selecting multiple stocks
tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS"]
ticker = st.selectbox("Select Stock Ticker", tickers)

# Fetch data from DB
query = f"SELECT * FROM stock_prices WHERE ticker='{ticker}'"
df = pd.read_sql(query, conn)

if not df.empty:
    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    # Show last 10 rows
    st.subheader("Recent Prices")
    st.write(df.tail(10))

    # Line chart for Close Price
    st.subheader("Stock Price Over Time")
    st.line_chart(df.set_index("timestamp")["close"])

    # Moving Average (20-period)
    df["MA20"] = df["close"].rolling(20).mean()
    st.subheader("Close Price + 20-period Moving Average")
    st.line_chart(df.set_index("timestamp")[["close", "MA20"]])

    # Volume chart
    st.subheader("Volume Over Time")
    st.bar_chart(df.set_index("timestamp")["volume"])

else:
    st.warning("No data found! Run stock_fetch_minute.py first.")

