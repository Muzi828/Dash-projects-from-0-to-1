import dash_bootstrap_components as dbc
from dash import html,Input,Output,dcc
from api import country_ls,updata_time,covid_data_2
import plotly.graph_objects as go
from app import app



ls = ['confirmed','death','recovered','active']

def IndicatorInfo():
    return dbc.Col(
        [
            html.H6('Select Country:',style={'paddingBottom':'20px'}),
            dcc.Dropdown(
                country_ls,
                'China',
                id = 'dpd'
            ),
            html.H6(f'New cases: {updata_time}',style={'paddingTop':'20px'}),
            html.Div(
                [
                    dcc.Graph(id=type,config={'displayModeBar': False}) for type in ls
                ],
            )
        ],width=2.5,className='card_container'
    )

def indicator(country,type,color):
    today_new_add = covid_data_2[covid_data_2['Country/Region'] == country].iloc[-1][type] - covid_data_2[covid_data_2['Country/Region'] == country].iloc[-2][type] 
    yesterday_new_add = covid_data_2[covid_data_2['Country/Region'] == country].iloc[-2][type] - covid_data_2[covid_data_2['Country/Region'] == country].iloc[-3][type] 

    fig = go.Figure(go.Indicator(
                title = {'text': f'New {type}','font': {'size': 15,'color':color}},
                mode = "number+delta",
                number = {'valueformat': ',',
                    'font': {'size': 15,'color':color}},
                value = today_new_add,
                delta = {'position': "right", 'reference': yesterday_new_add,'valueformat': ',',
                    'relative': False,
                    'font': {'size': 15}},
                domain = {'x': [0, 1], 'y': [0, 1]}))
                    
    fig.update_layout(
        paper_bgcolor='#182757',
        plot_bgcolor='#182757',
        font=dict(
        # family="Lato",
        size=18,
        color="white"),
        height = 75  #这个地方卡了很久，如果添加weight属性就不会居中，所以直接去掉就可
    )
 
    return fig

@app.callback(
    [Output(type,'figure') for type in ls],
    [Input('dpd','value')]
)
def update(value):
    return (
        indicator(value,'confirmed','orange'),
        indicator(value,'death','red'),
        indicator(value,'recovered','green'),
        indicator(value,'active','pink')
        )
    

    