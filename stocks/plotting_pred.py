# prediction_plotting.py

import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd

def plot_prediction_chart(forecast, stock_code):
    try:
        # Plot forecasted prices
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast', fill='tozeroy', line=dict(color='lightblue')))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill=None, mode='lines', line=dict(color='rgba(68, 68, 68, 0.1)'), name='Lower Bound'))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill='tonexty', mode='lines', line=dict(color='rgba(68, 68, 68, 0.1)'), name='Upper Bound'))
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
    fig.update_layout(title='Heikin Ashi Chart',
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


