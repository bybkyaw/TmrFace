# app.py

import streamlit as st
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

import yfinance as yf
import streamlit as st

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

# Display function in the sidebar with color-coded changes
def display_trending_stocks():

    st.sidebar.markdown("## Top Trending Stocks")
    trending_stocks = get_trending_stocks()  # Ensure this is fetching the correct data
    for stock in trending_stocks:
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

        st.sidebar.markdown(f"**{stock['symbol']}**: {price_display}{change_display}", unsafe_allow_html=True)

# Call this in your main app logic
display_trending_stocks()






