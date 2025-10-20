import sqlite3

# Connect to database (it will create stocks.db automatically if not exists)
conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

# Create table for stock prices
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_prices (
    timestamp TEXT,
    ticker TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER
)
""")

conn.commit()
conn.close()
print("Database and table created successfully!")
