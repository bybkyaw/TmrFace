import yfinance as yf
import streamlit as st
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import time
import yfinance as yf
import streamlit as st
import time

def get_trending_stocks():
    url = "https://finance.yahoo.com/trending-tickers/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='W(100%)')
    trending_stocks = []

    if table:
        rows = table.find_all('tr')[1:]  
        for row in rows:
            cols = row.find_all('td')
            symbol = cols[0].text.strip()
            name = cols[1].text.strip()
            current_price = get_live_stock_price(symbol)
            trending_stocks.append({'symbol': symbol, 'name': name, 'current_price': current_price})
            if len(trending_stocks) == 15:
                break

    return trending_stocks


# Function to get live stock price and change
def get_live_stock_price(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        
        hist = stock.history(period='2d')
        if len(hist) < 1:
            return None, None  

        live_price = hist['Close'].iloc[-1]
        if len(hist['Close']) > 1:
            previous_close = hist['Close'].iloc[-2]
        else:
            
            previous_close = live_price

        price_change = live_price - previous_close
        return live_price, price_change
    except Exception as e:
        print(f"Error fetching live stock price for {stock_code}: {e}")
        return None, None


#Display function in the sidebar with color-coded changes
def display_trending_stocks():
    st.sidebar.markdown("<h1 style='color:#4BB0FF;'>Top Trending Stocks</h1>", unsafe_allow_html=True)

    st.sidebar.markdown("&nbsp;") 
    st.markdown("<hr>", unsafe_allow_html=True)

    trending_stocks = get_trending_stocks()  # Ensure this is fetching the correct data

    # Create placeholders for live price display
    live_price_placeholders = []
    for stock in trending_stocks:
        live_price_placeholder = st.sidebar.empty()
        live_price_placeholders.append(live_price_placeholder)

    while True:
        for i, stock in enumerate(trending_stocks):
            live_price, price_change = get_live_stock_price(stock['symbol'])
            if live_price is not None:
                price_display = f"${live_price:.2f}"
                if price_change > 0:
                    change_display = f"<span style='color:green;'>+{price_change:.2f}</span>"
                elif price_change < 0:
                    change_display = f"<span style='color:red;'>{price_change:.2f}</span>"
                else:
                    change_display = ""
                change_display = f" ({change_display})" if price_change != 0 else ""
            else:
                price_display = "N/A"
                change_display = ""

            live_price_placeholders[i].markdown(f"**{stock['symbol']}**: {price_display}{change_display}",
                                                unsafe_allow_html=True)

        time.sleep(10)  
