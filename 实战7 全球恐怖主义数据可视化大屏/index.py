from dash import html
import dash_bootstrap_components as dbc
from app import app

from header import HeaderInfo
from filteritem import FilterInfo
from stackbarline import StackBarLineInfo
from piechart import PieInfo
from mapchart import MapInfo


app.layout = html.Div(
    [
        html.Div([HeaderInfo()]),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col([FilterInfo()],className='card_container'),
                        dbc.Col([StackBarLineInfo()],className='card_container'),
                        dbc.Col([PieInfo()],className='card_container')
                    ]
                )
            ]
        ),
        html.Div([MapInfo()],className='card_container',style={'marginLeft':0,'marginRight':5})
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)