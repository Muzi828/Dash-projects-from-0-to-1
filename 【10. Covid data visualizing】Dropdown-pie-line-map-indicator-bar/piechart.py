import dash_bootstrap_components as dbc
from dash import html,Input,Output,dcc
from app import app
from api import covid_data_2
import plotly.express as px

ls = ['confirmed','death','recovered','active']
def PieInfo():
    return dbc.Col(id = 'pie',width=4,className='card_container')

@app.callback(
    Output('pie','children'),
    [Input('dpd','value')]
)
def update(value):
    lastest_record = covid_data_2[covid_data_2['Country/Region'] == value].iloc[-1]
    fig = px.pie(values=[lastest_record[i] for i in ls],names=ls,hole=0.7)
    fig.update_layout(
        paper_bgcolor='#182757',
        plot_bgcolor='#182757',
        legend={
            'orientation':'h',
            'xanchor':'center',
            'yanchor':'bottom',
            'x':0.5,
            'y':-0.15
            },
        height=400,
        font=dict(
        # family="Lato",
        size=10,
        color="white"),
        margin=dict(
            t=30,
            b=30,
            l=30,
            r=30
        )
    )
    return [
        html.H6(f'Total Cases: {value}'),
        dcc.Graph(figure=fig,config={'displayModeBar': False})
    ]