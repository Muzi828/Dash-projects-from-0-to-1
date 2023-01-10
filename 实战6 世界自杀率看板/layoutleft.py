
from dash import html,dcc
from api import country_ls,year_min,year_max,age_ordered


def DropdownInfo():
    return html.Div(
        [
            html.H3('Select Country:'),
            dcc.Dropdown(
                country_ls,
                'Japan',
                id='dpd'
                )
        ]
    )


def RangeSliderInfo():
    return html.Div(
        [
            html.H3('Select Year:'),
            dcc.RangeSlider(
                year_min,year_max,1,
                marks=None,
                value=[1995,2005],
                tooltip={"placement": "bottom", "always_visible": True},
                id='rangeslider',
            )
        ],style={'paddingTop':'25px'}
    )

def ChecklistInfo():
    return html.Div(
        [
            html.H3('Select Platform:'),
            dcc.Checklist(
                age_ordered,
                ['35-54 years'],
                id = 'checklist',
                className = "columns"
            )
        ],style={'paddingTop':'25px'}
    )

