from dash import Dash,html
import dash_bootstrap_components as dbc
import pandas as pd
from app import app



from sidebar import SideBar
from tablebar import TableItem
from tabbar import TabItem
from infocards import InfoCards


app.layout = dbc.Row(
    [
        dbc.Col([SideBar()],width=3,className='bg-dark vh-100'),
        dbc.Col([InfoCards(),TabItem(),TableItem()],width=9)
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)