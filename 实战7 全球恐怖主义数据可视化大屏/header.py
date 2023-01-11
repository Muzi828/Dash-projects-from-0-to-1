from dash import html
from api import year_min,year_max

def HeaderInfo():
    return html.Div(
        [
            html.H1('Global Terrorism Database'),
            html.P(f'{year_min}-{year_max}')
        ],style={'paddingBottom':'30px','marginTop':'-50px'}
    )
