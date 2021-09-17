import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def ohlc(fn):
    df = pd.read_csv(fn)
    fig = go.Figure(data=go.Ohlc(
        x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close']))
    return fig


def colored_bar(fn):
    df = pd.read_csv(fn)
    fig = px.bar(df, x=df['date'], y=[df['open'],
                 df['low'], df['high'], df['close']], 
                color_discrete_sequence=px.colors.qualitative.Pastel1)
    return fig


def vertex_line(fn):
    df = pd.read_csv(fn)
    fig = go.Figure(go.Scatter(x=df['date'], y=df['close']))
    fig.update_layout(plot_bgcolor='pink', showlegend=True)
    return fig
