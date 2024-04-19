# get_live_stock.py

import yfinance as yf
import streamlit as st
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def get_live_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        live_price = stock.history(period="1d")['Close'][0]
        previous_close = stock.history(period="1d")['Close'][-2]
        price_change = live_price - previous_close
        return live_price, price_change
    except:
        return None, None
    


# Function to get live stock price and change
def get_live_stock_price(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        hist = stock.history(period='1d')
        print("Fetched historical data successfully:", hist)
        live_price = hist['Close'].iloc[-1]
        if len(hist) > 1:
            previous_close = hist['Close'].iloc[-2]
            price_change = live_price - previous_close
        else:
            # Get the last available closing price from the previous day
            yesterday = pd.Timestamp.now() - pd.Timedelta(days=1)
            hist_yesterday = stock.history(start=yesterday, end=yesterday)

            if len(hist_yesterday) > 0:
                previous_close = hist_yesterday['Close'].iloc[-1]
                price_change = live_price - previous_close
            else:
                price_change = 0  # No previous day data available
        return live_price, price_change
    except Exception as e:
        print("Error fetching live stock price:", e)
        return None, None



def get_trending_stocks():
    url = "https://finance.yahoo.com/trending-tickers/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='W(100%)')
    trending_stocks = []

    if table:
        rows = table.find_all('tr')[1:]  # Skipping the header row
        for row in rows:
            cols = row.find_all('td')
            symbol = cols[0].text.strip()
            name = cols[1].text.strip()
            current_price = get_live_stock_price(symbol)
            trending_stocks.append({'symbol': symbol, 'name': name, 'current_price': current_price})
            if len(trending_stocks) == 10:
                break

    return trending_stocks