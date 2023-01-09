import dash_bootstrap_components as dbc
from dash import html
from api import updata_time

def HeaderInfo():
    return dbc.Row(
        [
            dbc.Col(
                [
                    html.Img(src='assets/corona-logo-1.jpg',height='100px',width='100px')
                ],style = {'textAlign':'left','paddingTop':'1rem'}
            ),
            dbc.Col(
                [
                    html.H1('Covid - 19'),
                    html.H6('Track Covid - 19 Cases',className='p-2')
                ],style = {'textAlign':'center','paddingTop':'1rem'}
            ),
            dbc.Col(
                [
                    html.H5(f'Last Updated: {updata_time}'),
                    html.H5('00:01(UTC)',style={'paddingRight':'5rem'})
                ],style = {'textAlign':'right','paddingTop':'2rem','color':'orange'}
            ),
        ]
    )