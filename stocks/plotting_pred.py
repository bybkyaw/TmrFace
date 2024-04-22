# prediction_plotting.py

import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from prophet import Prophet
from datetime import datetime, timedelta
from stocks.stock_forecasting import forecast_stock_prices_1_week


def plot_prediction_chart(forecast, stock_code):
    try:
        # Detect when the trendline drops
        downturns = forecast['yhat'].diff() < 0

        # Plot forecasted prices
        fig = go.Figure()

        # Create gradient effects by layering fills
        for i in range(1, 6):  # Increase number for more layers and smoother gradient
            opacity = 0.1 + i * 0.02  # Gradually increasing opacity
            fillcolor = f'rgba(0, 187, 196, {opacity})'  # Adjust base color and opacity

            # Use lower part of the band to simulate gradient
            fig.add_trace(go.Scatter(
                x=forecast['ds'],
                y=forecast['yhat'] - i * forecast['yhat'].std() / 10,
                mode='lines',
                line=dict(color=fillcolor, width=0),
                fill='tonexty',
                fillcolor=fillcolor,
                showlegend=False
            ))

        # Add trendline with darker shades on downturns
        fig.add_trace(go.Scatter(
            x=forecast['ds'],
            y=forecast['yhat'],
            mode='lines',
            line=dict(color='#7DF9FF', width=2),
            name='Trendline',
            text=["Downturn" if down else "Normal" for down in downturns],
            hoverinfo="text+y"
        ))

        # Highlight downturns with a darker line
        if any(downturns):
            fig.add_trace(go.Scatter(
                x=forecast['ds'][downturns],
                y=forecast['yhat'][downturns],
                mode='lines',
                line=dict(color='#7DF9FF', width=2.5),
                showlegend=False
            ))

        fig.update_layout(title=f'Forecast for {stock_code}', xaxis_title='Date', yaxis_title='Price')

        return fig
    except Exception as e:
        print(f"Error plotting prediction chart: {e}")


def plot_heikin_ashi(ha_df):
    fig = go.Figure()

    # Plot candlesticks
    fig.add_trace(go.Candlestick(x=ha_df.index,
                                 open=ha_df['HA_Open'],
                                 high=ha_df['HA_High'],
                                 low=ha_df['HA_Low'],
                                 close=ha_df['HA_Close'],
                                 name='Heikin Ashi'))

    # Customize layout
    fig.update_layout(title='Hi & Lo',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=False)

    return fig


def calculate_heikin_ashi(df):
    ha_df = pd.DataFrame(index=df.index)
    ha_df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    
    # Initialize HA_Open to ensure there are no referencing issues
    ha_df['HA_Open'] = 0.0
    ha_df.at[df.index[0], 'HA_Open'] = (df.at[df.index[0], 'Open'] + df.at[df.index[0], 'Close']) / 2  # First row initial calculation
    
    # Sequentially calculate HA_Open for the rest of the rows
    for i in range(1, len(df)):
        ha_df.at[df.index[i], 'HA_Open'] = (ha_df.at[df.index[i-1], 'HA_Open'] + ha_df.at[df.index[i-1], 'HA_Close']) / 2

    # Calculate HA_High and HA_Low using max and min across specified columns
    ha_df['HA_High'] = df[['High']].join(ha_df[['HA_Open', 'HA_Close']]).max(axis=1)
    ha_df['HA_Low'] = df[['Low']].join(ha_df[['HA_Open', 'HA_Close']]).min(axis=1)

    return ha_df

def plot_candlestick_chart(forecast, stock_code):
    try:
        # Extract the necessary data for candlestick chart
        forecast_candlestick = forecast[['ds', 'yhat_lower', 'yhat_upper', 'yhat']]

        # Create a Plotly Candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=forecast_candlestick['ds'],
                                             open=forecast_candlestick['yhat'],
                                             high=forecast_candlestick['yhat_upper'],
                                             low=forecast_candlestick['yhat_lower'],
                                             close=forecast_candlestick['yhat'])])

        # Update layout
        fig.update_layout(title=f'Candlestick Chart for One Week Forecast of {stock_code}',
                          xaxis_title='Date',
                          yaxis_title='Price')

        return fig
    except Exception as e:
        print(f"Error plotting candlestick chart: {e}")




# def plot_rain_drop_chart(forecast, stock_code):
#     try:
#         # Filter the forecast data to include only the dates from today to one week ahead
#         today = datetime.now().date()
#         one_week_later = today + timedelta(days=7)
#         forecast_filtered = forecast[(forecast['ds'] >= today) & (forecast['ds'] <= one_week_later)]

#         # Plot the rain_drop chart using the filtered forecast data
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=forecast_filtered['ds'], y=forecast_filtered['yhat'], mode='lines', name='Rain Drop Forecast', line=dict(color='blue')))
#         fig.update_layout(title=f'Rain Drop Chart for {stock_code}', xaxis_title='Date', yaxis_title='Price')
#         return fig
#     except Exception as e:
#         print(f"Error plotting rain_drop chart: {e}")


# def plot_rain_drop_chart(forecast, stock_code):
#     try:
       
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast', fill='tozeroy', line=dict(color='lightblue')))
#         fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill=None, mode='lines', line=dict(color='rgba(68, 68, 68, 0.1)'), name='Lower Bound'))
#         fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill='tonexty', mode='lines', line=dict(color='rgba(68, 68, 68, 0.1)'), name='Upper Bound'))
#         fig.update_layout(title='Rain Drop Chart', xaxis_title='Date', yaxis_title='Price')
#         return fig
#     except Exception as e:
#         print(f"Error plotting rain drop chart: {e}")


