# col_1_stock.py

import streamlit as st
import yfinance as yf
from stock_lists import all_stocks, all_indices
from plotting import plot_live_stock_chart
from stock_info import get_open_price, get_previous_close_price, get_regular_market_change, get_day_high_price, get_day_low_price


# Function to get live stock price
def get_live_stock_price(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        live_price = stock.history(period='1d')['Close'].iloc[-1]
        return live_price
    except Exception as e:
        st.error(f"Error fetching live stock price: {e}")
        return None


# Function to get additional stock information
def get_stock_info(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        info = stock.info
        return info
    except Exception as e:
        st.error(f"Error fetching stock information: {e}")
        return None


# Main function for column 1 - live stock price and chart
def display_col1():
    # Sidebar layout with padding around the logo
    st.header("Live Stock Price and Chart")
    selected_stock = st.sidebar.selectbox('Select a stock for forecast', options=all_stocks + all_indices)

    # Display live stock price
    live_price = get_live_stock_price(selected_stock)
    if live_price:
        st.info(f"Current Price [{selected_stock}]: ${live_price}")

    # Plot live stock chart
    try:
        stock = yf.Ticker(selected_stock)
        hist = stock.history(period='1d')
        fig = plot_live_stock_chart(hist, selected_stock)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting live stock chart: {e}")


    # Expander to show/hide additional info
    with st.expander("More Info"):
        stock_info = get_stock_info(selected_stock)
        if stock_info:
            st.subheader("Market Summary")
            st.write(f"Selected Stock: {selected_stock}")
            st.write(f"Open Price: {stock_info.get('previousClose')}")
            st.write(f"Closed Price: {stock_info.get('stock_code')}")
            st.write(f"Difference Price: {stock_info.get('regularMarketChange')}")
            st.write(f"High Price: {stock_info.get('dayHigh')}")
            st.write(f"Low Price: {stock_info.get('dayLow')}")

