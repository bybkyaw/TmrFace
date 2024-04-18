# col_1_stock.py

import streamlit as st
import yfinance as yf
from news.col_2_news import display_col2
from stocks.stock_lists import all_stocks, all_indices
from stocks.stock_forecasting import forecast_stock_prices
from stocks.stock_info import get_live_stock_price
from stocks.stock_info_display import display_stock_info  
from stocks.plotting import plot_live_stock_chart
from stocks.plotting_pred import plot_prediction_chart

# Define selected_stock as global variable
selected_stock = "NVDA"

# Main function for column 1 - live stock price, chart, and forecast
def display_col1():
    global selected_stock  # Declare selected_stock as global

    # Sidebar layout with padding around the logo
    st.header("Live Stock Price and Chart")
    selected_stock = st.sidebar.selectbox('Select a stock', options = all_stocks + all_indices)

    
    # Display live stock price
    live_price = get_live_stock_price(selected_stock)
    if live_price:
        st.info(f"Current Price [{selected_stock}]: ${live_price}")

    # Plot live stock chart
    try:
        stock = yf.Ticker(selected_stock)
        hist = stock.history(period='1d')
        fig = plot_live_stock_chart(selected_stock)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting live stock chart: {e}")

    # Call function to display additional stock information
    display_stock_info(selected_stock, hist)  # Pass both selected_stock and hist to display_stock_info

    # Stock Forecasting section outside the expander
    st.header('Stock Forecast')

    if st.button(f'Show Forecast for {selected_stock}'):
        forecast, model = forecast_stock_prices(selected_stock)

        if forecast is not None:
            st.write(f"## Forecast for {selected_stock}")
            fig1 = plot_prediction_chart(forecast, selected_stock)  # Use plot_prediction_chart
            st.plotly_chart(fig1, use_container_width = True)
        else:
            st.error("Unable to fetch data for the selected stock.")

    return selected_stock






