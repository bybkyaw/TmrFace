# stock_info_display.py

import streamlit as st
from stock_info import get_stock_info

# Function to display additional stock information
def display_stock_info(selected_stock):
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
