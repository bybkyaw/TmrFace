# app.py

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from stocks.plotting import plot_live_stock_chart
from stocks.col_1_stock import display_col1
from news.col_2_news import display_col2
from stocks.get_live_stock import get_live_stock_price, get_trending_stocks

# Streamlit UI setup
st.set_page_config(page_title="TmrFace", page_icon="https://scalebranding.com/wp-content/uploads/2022/02/Duck-3.jpg", layout="wide")

# Sidebar layout with padding around the logo
st.sidebar.markdown(
    '<div style="padding: 0px 0px 0px 80px;"><img src="https://res.cloudinary.com/dom4dgtnf/image/upload/fl_preserve_transparency/v1713396766/DUCK_hcyr07.jpg?_s=public-apps" width="100" height="100"></div>',
    unsafe_allow_html=True
)  # Logo with padding

st.sidebar.markdown(
    '<div style="padding: 0px 0px 0 80px;"><h1>TmrFace</h1></div>', unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)


# Create two columns for layout
col1, col2 = st.columns([1, 1])

# In column 1: Display live stock price and chart
with col1:
    selected_stock = display_col1()

    # Store selected_stock in session state
    st.session_state.selected_stock = selected_stock

    st.markdown("<hr>", unsafe_allow_html=True)



# In column 2: Display news about the stock
with col2:
    display_col2(st.session_state.selected_stock)



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

def display_trending_stocks():
    st.sidebar.markdown("## Top Trending Stocks")
    trending_stocks = get_trending_stocks()

    for stock in trending_stocks:
        live_price, price_change = get_live_stock_price(stock['symbol'])

        if live_price is not None:
            price_display = f"<span style='color:#90B1DB;'>[${live_price:.2f}]</span>"
            if price_change > 0:
                change_display = f"<span style='color:green;'>[-{price_change:.2f}]</span>"
            elif price_change < 0:
                change_display = f"<span style='color:red;'>[+{price_change:.2f}]</span>"
            else:
                change_display = "[0.00]"

            # Display stock symbol
            st.sidebar.write(f"{stock['symbol']}  {price_display}   {change_display}", unsafe_allow_html=True)

            # Plot live stock chart and make it visible only on hover
            chart_id = f"chart_{stock['symbol']}"
            st.sidebar.write(f'<div id="{chart_id}" style="display: none;"></div>', unsafe_allow_html=True)
            script = f"""
            <script>
                var plotly_data = {plot_live_stock_chart(stock['symbol']).to_json()};
                Plotly.newPlot('{chart_id}', plotly_data.data, plotly_data.layout);
                document.getElementById("{stock['symbol']}").addEventListener("mouseover", function() {{
                    document.getElementById("{chart_id}").style.display = "block";
                }});
                document.getElementById("{stock['symbol']}").addEventListener("mouseout", function() {{
                    document.getElementById("{chart_id}").style.display = "none";
                }});
            </script>
            """
            st.sidebar.write(script, unsafe_allow_html=True)

# Call this in your main app logic
display_trending_stocks()


# def display_trending_stocks():
#     st.sidebar.markdown("## Top Trending Stocks")
#     trending_stocks = get_trending_stocks()

#     for stock in trending_stocks:
#         live_price, price_change = get_live_stock_price(stock['symbol'])

#         if live_price is not None:
#             price_display = f"<span style='color:lightblue;'>[${live_price:.2f}]</span>"
#             if price_change > 0:
#                 change_display = f"<span style='color:green;'>[-{price_change:.2f}]</span>"
#             elif price_change < 0:
#                 change_display = f"<span style='color:red;'>[+{price_change:.2f}]</span>"
#             else:
#                 change_display = "[0.00]"

#             # Plot the live stock chart
#             st.sidebar.write(f"{stock['symbol']}  {price_display}   {change_display}", unsafe_allow_html=True)
#             fig = plot_live_stock_chart(stock['symbol'])
#             if fig is not None:
#                 st.sidebar.plotly_chart(fig)

# # Call this in your main app logic
# display_trending_stocks()


# def display_trending_stocks():
#     st.sidebar.markdown("## Top Trending Stocks")
#     trending_stocks = get_trending_stocks()

#     for stock in trending_stocks:
#         live_price, price_change = get_live_stock_price(stock['symbol'])

#         if live_price is not None:
#             price_display = f"<span style='color:#93b9e1;'>[${live_price:.2f}]</span>"
#             if price_change > 0:
#                 change_display = f"<span style='color:green;'>[-{price_change:.2f}]</span>"
#             elif price_change < 0:
#                 change_display = f"<span style='color:red;'>[+{price_change:.2f}]</span>"
#             else:
#                 change_display = "[0.00]"
#         else:
#             price_display = "N/A"
#             change_display = ""

#         st.sidebar.markdown(f"{stock['symbol']}  {price_display}   {change_display}", unsafe_allow_html=True)

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
#         live_price, price_change = get_live_stock_price(stock['symbol'])

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

# # Call this in your main app logic
# display_trending_stocks()











