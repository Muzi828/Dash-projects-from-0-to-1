from dash import html
import dash_bootstrap_components as dbc
from app import app

from header import HeaderInfo
from middle import MiddleInfo
from bottom import BottomInfo

app.layout = html.Div(
    [
        html.Div([HeaderInfo()]),
        html.Div([MiddleInfo()]),
        html.Div([BottomInfo()])
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)