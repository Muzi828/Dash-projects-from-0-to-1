
from dash import html,dcc,Input,Output
import dash_bootstrap_components as dbc
from api import industry_list

def DropDownInfo():
    return dbc.Container(
        [
            html.H3('行业选择'),
            html.Hr(),
            dcc.Dropdown(
                industry_list,
                '食品',
                id = 'dpd'
            )
        ],className='py-2'
    )


def slider(name,min=-10,max=10,step=None,value=[-2,2]):
    return html.Div(
                [
                    html.H6(name),
                    dcc.RangeSlider(
                        min,max,step,
                        value = value,
                        marks=None,
                        id = name,
                        tooltip={"placement": "bottom", "always_visible": True}
                    )
                ]
            )

def RangeSliderInfo():
    return  dbc.Container(
        [
            html.H3('指数参数'),
            html.Hr(),
            slider('换手率'),
            slider('量比',min=0,max=10,value=[2,7])
        ],className='py-2'
    )





