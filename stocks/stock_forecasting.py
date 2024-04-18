# stock_forecasting.py

import yfinance as yf
from prophet import Prophet


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
