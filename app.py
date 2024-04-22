# app.py

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from time import sleep
from stocks.plotting import plot_live_stock_chart
from stocks.col_1_stock import display_col1
from news.col_2_news import display_col2
from stocks.get_live_stock import display_trending_stocks

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


display_trending_stocks()












