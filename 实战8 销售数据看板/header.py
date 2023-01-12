from dash import html,dcc
import dash_bootstrap_components as dbc
from api import year_ls,segment_ls

def HeaderInfo():
    year_min,year_max = min(year_ls),max(year_ls)

    return dbc.Row(
        [
            dbc.Col([html.H3('Sales Dashboard')]),
            dbc.Col([
                html.H6('销售年份'),
                dcc.Slider(
                min=year_min,max=year_max,step=1,
                value=max(year_ls),
                marks={str(yr): str(yr) for yr in range(year_min, year_max+1)},
                id='slider-year'
            )]),
            dbc.Col([
                    html.H6('Segment'),
                    dcc.RadioItems(
                        options=segment_ls,
                        value=segment_ls[0],
                        id='radio-segment'
                    )
                ]),
        ],style={'paddingBottom':'50px','marginTop':'-30px'}
    )
