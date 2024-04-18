# prediction_plotting.py

import plotly.graph_objs as go

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



# import plotly.graph_objs as go

# def plot_prediction_chart(forecast, stock_code):
#     try:
#         # Plot forecasted prices
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))
#         fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill=None, mode='lines', line=dict(color='rgba(68, 68, 68, 0.1)'), name='Lower Bound'))
#         fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill='tonexty', mode='lines', line=dict(color='rgba(68, 68, 68, 0.1)'), name='Upper Bound'))
#         fig.update_layout(title=f'Forecast for {stock_code}', xaxis_title='Date', yaxis_title='Price')
#         return fig
#     except Exception as e:
#         print(f"Error plotting prediction chart: {e}")
