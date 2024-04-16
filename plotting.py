# plotting.py

import plotly.express as px

def plot_live_stock_chart(hist, stock_code):
    try:
        fig = px.line(hist, x=hist.index, y='Close', title=f"Live Price Chart for {stock_code}")
        fig.update_traces(line=dict(color='blue'))  # Adjust line color
        fig.update_layout(
            xaxis_title="Time",
            yaxis_title="Price",
            hovermode="x unified",
            xaxis_rangeslider_visible=True,
            xaxis=dict(
                tickformat='%I:%M %p',  # Format for hours:minutes AM/PM
                range=[hist.index[0], hist.index[-1]]  # Adjusted data range for x-axis
            )
        )

        return fig
    except Exception as e:
        print(f"Error plotting live stock chart: {e}")
