import sqlite3
import pandas as pd
import os

# Database file
db_file = "stock_data.db"

# Connect to SQLite (creates DB if not exists)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_data (
    timestamp TEXT,
    ticker TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume REAL,
    daily_return REAL,
    moving_avg_5 REAL
)
""")
conn.commit()

# Processed data folder
processed_dir = "processed_data"

# Loop through each processed CSV file
for file_name in os.listdir(processed_dir):
    if file_name.endswith(".csv"):
        file_path = os.path.join(processed_dir, file_name)
        df = pd.read_csv(file_path)

        # ✅ Automatically use the first column as timestamp
        df.rename(columns={df.columns[0]: "timestamp"}, inplace=True)

        # ✅ Convert numeric columns to float
        numeric_cols = ["Open", "High", "Low", "Close", "Volume", "Daily_Return", "Moving_Avg_5"]
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

        # Drop rows with any NaN values
        df.dropna(inplace=True)

        # Extract ticker name from filename
        ticker = file_name.split("_")[0]

        # Insert each row into the database
        for _, row in df.iterrows():
            cursor.execute("""
            INSERT INTO stock_data (timestamp, ticker, open, high, low, close, volume, daily_return, moving_avg_5)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row['timestamp'],
                ticker,
                row['Open'],
                row['High'],
                row['Low'],
                row['Close'],
                row['Volume'],
                row['Daily_Return'],
                row['Moving_Avg_5']
            ))

conn.commit()
conn.close()
print(f"✅ All processed data loaded into database '{db_file}' successfully!")
