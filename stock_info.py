# stock_info.py

import yfinance as yf

# Function to get live stock price
def get_live_stock_price(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        live_price = stock.history(period='1d')['Close'].iloc[-1]
        return live_price
    except Exception as e:
        return None


# Function to get additional stock information

def get_stock_info(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        info = stock.info
        return info
    except Exception as e:
        return None

# Function to get open price
def get_open_price(stock_code):
    info = get_stock_info(stock_code)
    if info:
        return info.get('open')
    else:
        return None

# Function to get previous close price
def get_previous_close_price(stock_code):
    info = get_stock_info(stock_code)
    if info:
        return info.get('previousClose')
    else:
        return None

# Function to get regular market change
def get_regular_market_change(stock_code):
    info = get_stock_info(stock_code)
    if info:
        return info.get('regularMarketChange')
    else:
        return None

# Function to get day high price
def get_day_high_price(stock_code):
    info = get_stock_info(stock_code)
    if info:
        return info.get('dayHigh')
    else:
        return None

# Function to get day low price
def get_day_low_price(stock_code):
    info = get_stock_info(stock_code)
    if info:
        return info.get('dayLow')
    else:
        return None


