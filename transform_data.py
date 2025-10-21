import pandas as pd
import os

# Define folders
raw_dir = "raw_data"
processed_dir = "processed_data"
os.makedirs(processed_dir, exist_ok=True)

# Loop through each raw CSV file
for file in os.listdir(raw_dir):
    if file.endswith(".csv"):
        file_path = os.path.join(raw_dir, file)
        print(f"🔄 Processing: {file}")

        # Read the raw data
        df = pd.read_csv(file_path)

        # ✅ Convert text columns to numeric safely
        numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # ✅ Drop missing or invalid values
        df.dropna(inplace=True)

        # ✅ Add new calculated columns
        df["Daily_Return"] = df["Close"].pct_change()
        df["Moving_Avg_5"] = df["Close"].rolling(window=5).mean()

        # ✅ Remove any rows created by rolling window NaN
        df.dropna(inplace=True)

        # ✅ Save the transformed data
        processed_path = os.path.join(processed_dir, file)
        df.to_csv(processed_path, index=False)

        print(f"✅ Saved transformed file: {processed_path}")

print("\n🎯 Data transformation complete! All cleaned files are in the 'processed_data' folder.")
