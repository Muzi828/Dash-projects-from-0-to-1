from dash import html
from app import app
import dash_bootstrap_components as dbc


from header import HeaderInfo
from layoutleft import DropdownInfo,RangeSliderInfo,ChecklistInfo
from layoutright import Scatterchart

app.layout = html.Div(
    [
        html.Div([HeaderInfo()]),
        html.Div([
                dbc.Row(
                [
                    dbc.Col([DropdownInfo(),RangeSliderInfo(),ChecklistInfo()],width=4,className='card_container'),
                    dbc.Col([Scatterchart()],className='card_container')
                ]
            )
        ])
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)



