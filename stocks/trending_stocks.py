# trending_stocks.py

import streamlit as st
import yfinance as yf
from stock_lists import all_stocks, all_indices

# Function to get trending stocks and indices
def get_trending_stocks():
    # Fetch live data for trending stocks and indices
    trending_stocks = {}
    for stock_code in all_stocks + all_indices:
        stock = yf.Ticker(stock_code)
        info = stock.info
        price = info.get('regularMarketPrice')
        change = info.get('regularMarketChange')
        trending_stocks[stock_code] = {'price': price, 'change': change}

    # Sort trending stocks based on change
    trending_stocks = dict(sorted(trending_stocks.items(), key=lambda item: item[1]['change'], reverse=True))
    
    return trending_stocks

# Function to display trending stocks in the sidebar
def display_trending_stocks():
    st.sidebar.title("Trending Live Stocks")

    trending_stocks = get_trending_stocks()
    for stock_code, data in trending_stocks.items():
        price = data['price']
        change = data['change']

        if change > 0:
            change_color = "green"
        elif change < 0:
            change_color = "red"
        else:
            change_color = "white"

        st.sidebar.write(f"{stock_code}: ${price}  ", unsafe_allow_html=True)
        st.sidebar.markdown(f"<span style='color:{change_color}'>{change}</span>", unsafe_allow_html=True)
