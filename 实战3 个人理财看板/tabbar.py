

from dash import Dash,html,Output,Input,dcc
import dash_bootstrap_components as dbc
import pandas as pd
from dash import  dash_table
from app import app
import plotly.express as px
import os

def TabItem():
    return html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="月账单", tab_id="tab-1"),
                dbc.Tab(label="年账单", tab_id="tab-2"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div([MonthBar()],id="content"),
    ]
)


def MonthBar():
    fig = px.bar()
    return dcc.Graph(figure=fig,id='chart')


def YearBar():
    total = []
    for i in os.listdir('实战3 个人理财看板/data'):
        df = pd.read_excel(f'实战3 个人理财看板/data/{i}')
        month_total = sum(df.sum().to_list())
        total.append(month_total)
    fig = px.bar(x=[f'{i}月' for i in range(1,13)],y=total,range_y=[0,9000])
    return dcc.Graph(figure=fig)


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return MonthBar()
    elif at == "tab-2":
        return YearBar()

@app.callback(Output('chart','figure'),[Input('table','data')])
def update(v):
    df = pd.DataFrame(v)
    data = df.sum().to_list()
    return px.bar(x = df.columns,y=data,range_y= [0,4000])
    