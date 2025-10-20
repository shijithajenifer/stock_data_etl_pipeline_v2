# 📈 Real-Time Stock Dashboard

Project Overview

    This project is a **real-time stock price dashboard** built using **Python**, **SQLite**, and **Streamlit**.  
    It fetches stock data from the `yfinance` API, stores it in a **SQLite database**, and visualizes it interactively.  

The dashboard allows users to:  
- View recent stock prices  
- Plot **Close Price** over time  
- Plot **20-period Moving Average**  
- Plot **Volume**  
- Select multiple stocks using a dropdown  

This mini-project demonstrates a complete **data engineering pipeline** from **data extraction → storage → visualization**.

## Features
- Minute-level stock data extraction using `yfinance`  
- SQLite database storage for efficient data management  
- Interactive Streamlit dashboard  
- Moving Average analysis  
- Volume visualization  
- Dropdown to select multiple stocks  

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| Python | Main programming language |
| yfinance | Fetch stock data from Yahoo Finance |
| SQLite | Store stock data |
| Pandas | Data processing and analysis |
| Streamlit | Dashboard visualization |
| VS Code | Development environment |

## Installation & Usage

1. **Clone the repository**

git clone https://github.com/shijithajenifer/stock-dashboard.git

cd stock_project

2. Create virtual environment

     python -m venv venv

3.Activate virtual environment

     # Windows PowerShell
     venv\Scripts\Activate.ps1

4.Install dependencies

     pip install yfinance pandas matplotlib streamlit

5.Fetch stock data

     python stock_fetch_minute.py

6.Run the dashboard

     streamlit run dashboard.py

7.Open the browser to interact with the dashboard

Future Enhancements

   -  Compare multiple stocks in a single chart
   -  Auto-refresh data for live updates
   -  Add predictive analytics
   -  Deploy dashboard online using Streamlit Cloud