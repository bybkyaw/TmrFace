# stock_info_display.py

import streamlit as st
from stocks.stock_info import get_stock_info

# Function to display additional stock information
def display_stock_info(selected_stock, hist):

    with st.expander("More Info"):
        stock_info = get_stock_info(selected_stock)

        if stock_info:
            st.subheader("Stock Price Summary")
            st.write(f"Selected Stock: {selected_stock}")
            

            # Display historical data
            st.markdown(f"### Today  <span style='color:lightblue'>{selected_stock}</span> Data", unsafe_allow_html=True)
            st.write(hist)



