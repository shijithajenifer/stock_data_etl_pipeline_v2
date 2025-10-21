# 📊 Stock Data ETL Pipeline

**Real-time Stock Data Extraction, Transformation, Loading, and Visualization Project**

---

## **Project Overview**

This project demonstrates a complete **Data Engineering ETL pipeline** for stock market data. It fetches stock data in real-time, cleans and transforms it, calculates key metrics, stores it in a database, and visualizes insights through an interactive dashboard. Perfect for building your **portfolio and impressing recruiters**.

---

## **ETL Pipeline Steps**

1. **Extract (fetch_raw_data.py / stock_fetch_minute.py)**

   * Fetches minute-level stock data from Yahoo Finance using Python `yfinance`.

2. **Transform (transform_data.py)**

   * Cleans raw data, calculates **Daily Returns** and **5-day Moving Averages**.

3. **Load (load_to_db.py)**

   * Loads transformed data into **SQLite database** (`stock_data.db`).

4. **Visualize (dashboard.py)**

   * Interactive **Streamlit dashboard** showing:

     * Stock close prices
     * Daily returns
     * Moving averages
   * Users can select different tickers from the sidebar.

---

## **Tech Stack**

* Python
* Pandas
* SQLite
* Streamlit
* Matplotlib & Seaborn


## **How to Run**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/stock_data_etl_pipeline_v2.git
cd stock_data_etl_pipeline_v2
```

2. Activate virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run ETL pipeline:

```bash
python stock_fetch_minute.py
python transform_data.py
python load_to_db.py
```

5. Run the dashboard:

```bash
streamlit run dashboard.py
```

---

## **Outcome**

* Fully automated **stock data ETL pipeline**.
* Interactive visualization dashboard for stock analysis.
* Resume & portfolio-ready Data Engineering project.
