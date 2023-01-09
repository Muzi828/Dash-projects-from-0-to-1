from dash import html,Input,Output,dcc
from app import app
from api import geo_data
import plotly.express as px
import dash_bootstrap_components as dbc

def MapInfo():

    #考虑到测试计算机的性能，可以指定数据采样，比如只取十分之一的数据进行演示
    geo_data_resample = geo_data.sample(frac = 0.1)

    fig = px.choropleth(geo_data_resample.sort_values('date_play'),               
                                locations="iso",               
                                color="confirmed",
                                hover_name="Country/Region",  
                                animation_frame="date_play",    
                                color_continuous_scale='amp',  
                                height=600)

    fig.update_layout(
        paper_bgcolor='#182757',
        plot_bgcolor='#182757',
        font=dict(
        # family="Lato",
        size=14,
        color="white"),
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
        )
    )
    return dbc.Col(
        [
            dcc.Graph(figure= fig)
        ],className='card_container'
    )


