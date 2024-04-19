# # trending_stocks.py

# import streamlit as st
# import yfinance as yf
# from stocks.get_live_stock import get_trending_stocks

# # Function to get live stock price and change
# def get_live_trend_stock_price(stock_code):
#     try:
#         stock = yf.Ticker(stock_code)

#         # Getting the last 2 days to ensure we have a previous close in case of missing data
#         hist = stock.history(period='2d')
#         if len(hist) < 1:
#             return None, None  # In case no data is returned

#         live_price = hist['Close'].iloc[-1]
#         if len(hist['Close']) > 1:
#             previous_close = hist['Close'].iloc[-2]
#         else:
#             # If we only have one day of data, no change can be calculated
#             previous_close = live_price
        
#         price_change = live_price - previous_close
#         return live_price, price_change
#     except Exception as e:
#         print(f"Error fetching live stock price for {stock_code}: {e}")
#         return None, None


# def display_trending_stocks():
#     st.sidebar.markdown("## Top Trending Stocks")
#     trending_stocks = get_trending_stocks()

#     symbols = []
#     prices = []
#     changes = []

#     # Fetch data for each trending stock
#     for stock in trending_stocks:
#         live_price, price_change = get_live_trend_stock_price(stock['symbol'])

#         if live_price is not None:
#             symbols.append(stock['symbol'])
#             prices.append(f"${live_price:.2f}")

#             if price_change > 0:
#                 changes.append(f"[ +{price_change:.2f} ]")
#             elif price_change < 0:
#                 changes.append(f"[ {price_change:.2f} ]")
#             else:
#                 changes.append("[ 0.00 ]")
#         else:
#             symbols.append(stock['symbol'])
#             prices.append("N/A")
#             changes.append("")

#     # Determine maximum lengths for alignment
#     max_symbol_length = max(len(symbol) for symbol in symbols)
#     max_price_length = max(len(price) for price in prices)
#     max_change_length = max(len(change) for change in changes)

#     # Header alignment with horizontal line
#     st.sidebar.markdown(f"{'Symbol':<{max_symbol_length}}    {'Price':<{max_price_length}}            {'Change':<{max_change_length}}")
#     st.sidebar.markdown("______________________________")

#     # Data alignment
#     for symbol, price, change in zip(symbols, prices, changes):
#         st.sidebar.markdown(f"{symbol:<{max_symbol_length}}    {price:<{max_price_length}}        {change:<{max_change_length}}", unsafe_allow_html=True)

# # Call this in your main app logic
# display_trending_stocks()


# # Function for Displaying Trending Stock
# def display_trending_stocks():
#     st.sidebar.markdown("## Top Trending Stocks")
#     trending_stocks = get_trending_stocks()

#     symbols = []
#     prices = []
#     changes = []

#     # Fetch data for each trending stock
#     for stock in trending_stocks:
#         live_price, price_change = get_live_trend_stock_price(stock['symbol'])

#         if live_price is not None:
#             symbols.append(stock['symbol'])
#             prices.append(f"${live_price:.2f}")

#             if price_change > 0:
#                 changes.append(f"<span style='color:green;'>+{price_change:.2f}</span>")
#             elif price_change < 0:
#                 changes.append(f"<span style='color:red;'>{price_change:.2f}</span>")
#             else:
#                 changes.append("")
#         else:
#             symbols.append(stock['symbol'])
#             prices.append("N/A")
#             changes.append("")

#     # Determine maximum lengths for alignment
#     max_symbol_length = max(len(symbol) for symbol in symbols)
#     max_price_length = max(len(price) for price in prices)
#     max_change_length = max(len(change) for change in changes)

#     # Header alignment with horizontal line
#     st.sidebar.markdown(f"{'Symbol':<{max_symbol_length}}  {'Price':<{max_price_length + 5}}    {'Change':<{max_change_length + 5}}")
#     st.sidebar.markdown(f"{'-' * max_symbol_length}  {'-' * (max_price_length + 5)}    {'-' * (max_change_length + 5)}")

#     # Data alignment
#     for symbol, price, change in zip(symbols, prices, changes):
#         st.sidebar.markdown(f"{symbol:<{max_symbol_length}}  {price:<{max_price_length + 5}}    {change:<{max_change_length + 5}}", unsafe_allow_html=True)
