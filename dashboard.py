import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite DB
conn = sqlite3.connect("stock_data.db")

st.title("📈 Stock Data Dashboard")
st.write("Visualizing processed stock data from your ETL pipeline")

# Get list of unique tickers
tickers = pd.read_sql("SELECT DISTINCT ticker FROM stock_data", conn)
ticker_list = tickers['ticker'].tolist()

# Sidebar to select ticker
selected_ticker = st.sidebar.selectbox("Select Ticker", ticker_list)

# Fetch data for selected ticker
query = f"SELECT * FROM stock_data WHERE ticker='{selected_ticker}'"
df = pd.read_sql(query, conn)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot Close Price
st.subheader(f"{selected_ticker} Close Price")
plt.figure(figsize=(10,4))
sns.lineplot(x='timestamp', y='close', data=df)
plt.xticks(rotation=45)
st.pyplot(plt)

# Plot Moving Average
st.subheader(f"{selected_ticker} 5-Day Moving Average")
plt.figure(figsize=(10,4))
sns.lineplot(x='timestamp', y='moving_avg_5', data=df)
plt.xticks(rotation=45)
st.pyplot(plt)

# Plot Daily Return
st.subheader(f"{selected_ticker} Daily Return")
plt.figure(figsize=(10,4))
sns.lineplot(x='timestamp', y='daily_return', data=df)
plt.xticks(rotation=45)
st.pyplot(plt)

conn.close()
