# stock_forecasting.py

import pandas as pd
import yfinance as yf
from prophet import Prophet
from datetime import datetime, timedelta


# Forecasting function using Prophet
def forecast_stock_prices(stock_code):
    data = yf.download(stock_code, period = '2y')

    if data.empty:
        return None, "Data is empty."
    df = data.reset_index()[['Date', 'Close']].rename(columns = {'Date': 'ds', 'Close': 'y'})
    model = Prophet(daily_seasonality = True)
    model.fit(df)
    future = model.make_future_dataframe(periods = 30)
    forecast = model.predict(future)
    return forecast, model


# Forecasting function using Prophet for 1 week
def forecast_stock_prices_1_week(stock_code):
    
    start_date = datetime.now().date() - timedelta(days=365 * 2)  # 2 years of historical data
    end_date = datetime.now().date()

    data = yf.download(stock_code, start=start_date, end=end_date)

    if data.empty:
        return None, "Data is empty."

    # Select only the last week of data for training
    df = data.reset_index()[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
    df = df.tail(7 + 7)  # Selecting 14 days (7 days for training + 7 days for prediction)

    model = Prophet(daily_seasonality=True)
    model.fit(df)
    future = model.make_future_dataframe(periods=7)  # Forecasting for 1 week (7 days)
    forecast = model.predict(future)
    return forecast, model
