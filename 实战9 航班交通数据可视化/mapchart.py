from dash import html,dcc,Input,Output
from app import app
import plotly.express as px
from api import state_airport_data

def MapchartInfo():
    return html.Div(
        [
            dcc.Graph(id='map-chart')
        ]
    )

@app.callback(
    Output('map-chart','figure'),
    [Input('dpd','value')]
)
def update(state):
    df = state_airport_data[state_airport_data['state']==state]
    fig=px.scatter_mapbox(df,lat=df['lat'],lon=df['long'],
                            color=df['cnt'],
                            size=df['cnt']*50,zoom=4)
    fig.update_layout(
        title={'text': f'Total Arrivals in {state} State',
                   'y': 0.99,
                   'x': 0.4,
                   'xanchor': 'left',
                   'yanchor': 'top'},
        paper_bgcolor = '#262626',
        plot_bgcolor = '#262626',
        font = {'family':'sans-serif','color':'white','size':12},
        margin=dict(r=0, l =0, b = 0, t = 30),
        mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',
                style='dark',
            ),
    )
    return fig
