from dash import html
from app import app
import dash_bootstrap_components as dbc

from sider import SiderInfo
from mapchart import MapchartInfo
from barchart import BarchartInfo


app.layout = html.Div(
    dbc.Row(
        [
            dbc.Col([SiderInfo()],width=3,className='border-right border-dark vh-100 sider'),
            dbc.Col([MapchartInfo(),BarchartInfo()]),
        ]
    )
) 

if __name__ == '__main__':
    app.run_server(debug=True)
