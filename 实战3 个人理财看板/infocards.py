import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output,Input
from app import app
from dash import html
from datainfo import seadon_dict,year_total,year_ls 
import pandas as pd

def card(name,cost,color):
    return html.Div([
        html.H3(name),
        html.Hr(),
        html.H1(cost,id=name)
    ],className=f'{color} text-white rounded p-4'
    )

def InfoCards():
    return dbc.Row(
        [
            dbc.Col(card('月份花销','---','bg-info')),
            dbc.Col(card('季度花销','---','bg-warning')),
            dbc.Col(card('年份花销','---','bg-primary')),
        ],className='py-4'
    )

@app.callback(
    [Output('月份花销','children'),Output('季度花销','children'),Output('年份花销','children')],
    [Input('dpd','value')])
def update(v):

    df = pd.read_excel(f'实战3 个人理财看板/data/{v}')
    month_total = sum(df.sum().to_list())
    season_total = 0
    for i in seadon_dict.values():
        if int(v[:-8]) in i:
            season_total = year_ls[i[0]]+year_ls[i[1]]+year_ls[i[2]]
    return (month_total,season_total,year_total)
