
from dash import html
import dash_bootstrap_components as dbc
from api import *

def card(type,num,diff,color):

    if num == 'No data available':
        diff_per = 'No data available'
    else:
        diff_per = diff/num * 100

    return dbc.Col(
        [
            html.H6(f'Global {type}'),
            html.H2(num,style={'color':color}),
            html.P(f'New {int(diff)} ({diff_per:.2f})%',style={'color':color,'fontSize':5})
        ],className='card_container',style={'paddingTop':30}
    )

def CardInfo():
    return dbc.Row(
        [
            card('cases',confirmed_num,rate_confirmed,'orange'),
            card('death',death_num,rate_death,'red'),
            card('recovered',recovered_num,rate_recovered,'green'),
            card('active',active_num,rate_active,'pink')
        ]
    )