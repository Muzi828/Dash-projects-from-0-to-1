from dash import html,dcc,Input,Output
import dash_bootstrap_components as dbc
from app import app
import pandas as pd
import plotly.graph_objects as go
from api import pro,start_date,end_date

def FigureInfo():
    return dbc.Container('',id='content')

def plain_style(fig):
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#233552", zeroline=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#233552", zeroline=False)
    fig.update_layout(
        margin=dict(
        l=0,
        r=25,
        b=0,
        t=25,
        pad=0
        ),
        xaxis_rangeslider_visible=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=450,
        font_color="#7F9BB4",)
    return fig


@app.callback(
    Output('content','children'),
    [Input('table','active_cell'),Input('table','data')]
)
def update(v1,v2):
    v1 = pd.DataFrame(v2).iloc[v1['row'],0] if v1 is not None else v2[0]['股票代码']
    
    df = pro.daily(ts_code=v1, start_date=start_date, end_date=end_date)

    fig = go.Figure(
                    data=[
                        go.Candlestick(x=df['trade_date'],
                                        open=df['open'],
                                        high=df['high'],
                                        low=df['low'],
                                        close=df['close'])
                    ]
    )
    fig = plain_style(fig)

    return dbc.Container(
        [
            html.H3(f'股票代码：{v1}'),
            dcc.Graph(
                figure = fig
            )
        ],className='py-2'
    )
    
