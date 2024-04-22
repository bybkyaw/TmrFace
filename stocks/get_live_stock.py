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
#
#
#
# # Function to get live stock price and change
# def get_live_stock_price(stock_code):
#     try:
#         stock = yf.Ticker(stock_code)
#         hist = stock.history(period='1d')
#         print("Fetched historical data successfully:", hist)
#         live_price = hist['Close'].iloc[-1]
#         if len(hist) > 1:
#             previous_close = hist['Close'].iloc[-2]
#             price_change = live_price - previous_close
#         else:
#             # Get the last available closing price from the previous day
#             yesterday = pd.Timestamp.now() - pd.Timedelta(days=1)
#             hist_yesterday = stock.history(start=yesterday, end=yesterday)
#             if len(hist_yesterday) > 0:
#                 previous_close = hist_yesterday['Close'].iloc[-1]
#                 price_change = live_price - previous_close
#             else:
#                 price_change = 0  # No previous day data available
#         return live_price, price_change
#     except Exception as e:
#         print("Error fetching live stock price:", e)
#         return None, None
#
#
#
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





# Function to get live stock price and change
def get_live_stock_price(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        # Getting the last 2 days to ensure we have a previous close in case of missing data
        hist = stock.history(period='2d')
        if len(hist) < 1:
            return None, None  # In case no data is returned

        live_price = hist['Close'].iloc[-1]
        if len(hist['Close']) > 1:
            previous_close = hist['Close'].iloc[-2]
        else:
            # If we only have one day of data, no change can be calculated
            previous_close = live_price

        price_change = live_price - previous_close
        return live_price, price_change
    except Exception as e:
        print(f"Error fetching live stock price for {stock_code}: {e}")
        return None, None


#Display function in the sidebar with color-coded changes
def display_trending_stocks():
    st.sidebar.markdown("## Top Trending Stocks")
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

        time.sleep(10)  # Update every 30 seconds





# Display function in the sidebar with color-coded changes
# def display_trending_stocks():
#     st.sidebar.markdown("## Top Trending Stocks")
#     trending_stocks = get_trending_stocks()  # Ensure this function fetches current trending stock data
#
#     for stock in trending_stocks:
#         live_price, price_change = get_live_stock_price(stock['symbol'])
#         if live_price is not None:
#             price_display = f"${live_price:.2f}"
#             if price_change > 0:
#                 change_display = f"<span style='color:green;'>+{price_change:.2f}</span>"
#             elif price_change < 0:
#                 change_display = f"<span style='color:red;'>{price_change:.2f}</span>"
#             else:
#                 change_display = "<span style='color:black;'>0.00</span>"
#         else:
#             price_display = "N/A"
#             change_display = "<span style='color:black;'>N/A</span>"
#
#         # Displaying with some HTML for better formatting
#         st.sidebar.markdown(f"<div style='display: flex; justify-content: space-between; align-items: center; font-size: 16px; margin: 5px 0;'><div>{stock['symbol']}</div><div>{price_display}</div><div>{change_display}</div></div>", unsafe_allow_html=True)
#
#     # Rerun the app every minute to update the prices
#     if 'counter' not in st.session_state:
#         st.session_state.counter = 0
#     st.session_state.counter += 1
#     if st.session_state.counter > 5:  # Reset counter periodically if you want
#         st.session_state.counter = 0
#     st.experimental_rerun()