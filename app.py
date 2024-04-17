# app.py

import streamlit as st
import stock_lists
from col_1_stock import display_col1
from col_2_news import display_col2
from stock_lists import all_stocks, all_indices

# Streamlit UI setup
st.set_page_config(page_title="TmrFace", page_icon=":chart_with_upwards_trend:", layout="wide")

# Sidebar layout with padding around the logo
st.sidebar.markdown(
    '<div style="padding: 0px 0px 0px 80px;"><img src="TF_Logo.png" width="100" height="100"></div>', unsafe_allow_html=True)  # Logo with padding
st.sidebar.markdown(
    '<div style="padding: 0px 0px 0 80px;"><h1>TmrFace</h1></div>', unsafe_allow_html=True)

# Display columns
col1, col2 = st.columns([1, 1])
with col1:
    display_col1()

with col2:
    display_col2()
