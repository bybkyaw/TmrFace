# col_1_stock.py

import streamlit as st
import yfinance as yf
from stock_lists import all_stocks, all_indices
from stock_forecasting import forecast_stock_prices
from plotting import plot_live_stock_chart
from stock_info import get_live_stock_price, get_stock_info
from plotting_pred import plot_prediction_chart  # Updated import statement

# Main function for column 1 - live stock price, chart, and forecast
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

    # Stock Forecasting section outside the expander
    st.header('Stock Forecast')
    if st.button(f'Show Forecast for {selected_stock}'):
        forecast, model = forecast_stock_prices(selected_stock)
        if forecast is not None:
            st.write(f"## Forecast for {selected_stock}")
            fig1 = plot_prediction_chart(forecast, selected_stock)  # Use plot_prediction_chart
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.error("Unable to fetch data for the selected stock.")




# import streamlit as st
# import yfinance as yf
# from stock_lists import all_stocks, all_indices
# from stock_forecasting import forecast_stock_prices
# from plotly import graph_objs as go  # Import Plotly
# from plotting import plot_live_stock_chart  # Ensure this function is defined in plotting.py
# from stock_info import get_live_stock_price, get_stock_info

# # Main function for column 1 - live stock price, chart, and forecast
# def display_col1():
#     # Sidebar layout with padding around the logo
#     st.header("Live Stock Price and Chart")
#     selected_stock = st.sidebar.selectbox('Select a stock for forecast', options=all_stocks + all_indices)

#     # Display live stock price
#     live_price = get_live_stock_price(selected_stock)
#     if live_price:
#         st.info(f"Current Price [{selected_stock}]: ${live_price}")

#     # Plot live stock chart
#     try:
#         stock = yf.Ticker(selected_stock)
#         hist = stock.history(period='1d')
#         fig = plot_live_stock_chart(hist, selected_stock)
#         st.plotly_chart(fig)
#     except Exception as e:
#         st.error(f"Error plotting live stock chart: {e}")

#     # Expander to show/hide additional info
#     with st.expander("More Info"):
#         stock_info = get_stock_info(selected_stock)
#         if stock_info:
#             st.subheader("Market Summary")
#             st.write(f"Selected Stock: {selected_stock}")
#             st.write(f"Open Price: {stock_info.get('previousClose')}")
#             st.write(f"Closed Price: {stock_info.get('stock_code')}")
#             st.write(f"Difference Price: {stock_info.get('regularMarketChange')}")
#             st.write(f"High Price: {stock_info.get('dayHigh')}")
#             st.write(f"Low Price: {stock_info.get('dayLow')}")

#             # Forecasting section
#             st.header('Stock Forecast')
#             if st.button(f'Show Forecast for {selected_stock}'):
#                 forecast, model = forecast_stock_prices(selected_stock)
#                 if forecast is not None:
#                     st.write(f"## Forecast for {selected_stock}")
#                     fig1 = plot_plotly(model, forecast)
#                     st.plotly_chart(fig1, use_container_width=True)
#                     fig2 = plot_components_plotly(model, forecast)
#                     st.plotly_chart(fig2, use_container_width=True)
#                 else:
#                     st.error("Unable to fetch data for the selected stock.")


# # col_1_stock.py

# import streamlit as st
# import yfinance as yf
# from stock_lists import all_stocks, all_indices
# from stock_forecasting import forecast_stock_prices
# from plotting import plot_live_stock_chart
# from stock_info import get_live_stock_price, get_stock_info


# # Main function for column 1 - live stock price, chart, and forecast
# def display_col1():
#     # Sidebar layout with padding around the logo
#     st.header("Live Stock Price and Chart")
#     selected_stock = st.sidebar.selectbox('Select a stock for forecast', options=all_stocks + all_indices)

#     # Display live stock price
#     live_price = get_live_stock_price(selected_stock)
#     if live_price:
#         st.info(f"Current Price [{selected_stock}]: ${live_price}")

#     # Plot live stock chart
#     try:
#         stock = yf.Ticker(selected_stock)
#         hist = stock.history(period='1d')
#         fig = plot_live_stock_chart(hist, selected_stock)
#         st.plotly_chart(fig)
#     except Exception as e:
#         st.error(f"Error plotting live stock chart: {e}")

#     # Expander to show/hide additional info
#     with st.expander("More Info"):
#         stock_info = get_stock_info(selected_stock)
#         if stock_info:
#             st.subheader("Market Summary")
#             st.write(f"Selected Stock: {selected_stock}")
#             st.write(f"Open Price: {stock_info.get('previousClose')}")
#             st.write(f"Closed Price: {stock_info.get('stock_code')}")
#             st.write(f"Difference Price: {stock_info.get('regularMarketChange')}")
#             st.write(f"High Price: {stock_info.get('dayHigh')}")
#             st.write(f"Low Price: {stock_info.get('dayLow')}")

#             # Forecasting section
#             st.header('Stock Forecast')
#             if st.button(f'Show Forecast for {selected_stock}'):
#                 forecast, model = forecast_stock_prices(selected_stock)
#                 if forecast is not None:
#                     st.write(f"## Forecast for {selected_stock}")
#                     fig1 = plot_plotly(model, forecast)
#                     st.plotly_chart(fig1, use_container_width=True)
#                     fig2 = plot_components_plotly(model, forecast)
#                     st.plotly_chart(fig2, use_container_width=True)
#                 else:
#                     st.error("Unable to fetch data for the selected stock.")



