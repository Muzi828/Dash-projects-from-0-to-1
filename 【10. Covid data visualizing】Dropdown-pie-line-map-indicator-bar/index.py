from app import app
from dash import html
import dash_bootstrap_components as dbc

from header import HeaderInfo
from cards import CardInfo
from indicators import IndicatorInfo
from piechart import PieInfo
from barlinechart import BarLineInfo
from mapchart import MapInfo


app.layout = html.Div(
    [
        html.Div([HeaderInfo()]),
        html.Div([CardInfo()]),
        html.Div([dbc.Row([IndicatorInfo(),PieInfo(),BarLineInfo()])]),
        html.Div([MapInfo()],style={'marginLeft':-15,'marginRight':15}),
    ],className='div_container'
)

if __name__ == '__main__':
    app.run_server(debug=True)