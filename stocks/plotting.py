import yfinance as yf
import plotly.graph_objects as go

def plot_live_stock_chart(stock_code):
    try:
        stock_data = yf.Ticker(stock_code)
        hist = stock_data.history(period = "1d", interval = '1m')  
        print(hist.head())  
        print("Data columns:", hist.columns)  

        if hist.empty:
            print("No data retrieved.")
            return None

        # Create the plot with green line color
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = hist.index, y = hist['Close'], mode = 'lines', name = 'Close Price', line = dict(color = 'lightblue')))
        fig.update_layout(
            title = f"Live Price Chart for {stock_code}",
            xaxis_title = "Time",
            yaxis_title = "Price",
            hovermode = "x unified",
            xaxis_rangeslider_visible = True,
            xaxis = dict(
                tickformat='%I:%M %p',
                range=[hist.index[0], hist.index[-1]] if not hist.index.empty else None
            )
        )

        return fig
    except Exception as e:
        print(f"Error plotting live stock chart: {e}")
        return None
