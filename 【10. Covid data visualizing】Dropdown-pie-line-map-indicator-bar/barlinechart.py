import dash_bootstrap_components as dbc
from dash import html,Input,Output,dcc
from app import app
from api import get_30_days_data
import plotly.graph_objects as go

def BarLineInfo():
    return dbc.Col(id='barline',className='card_container')

@app.callback(
    Output('barline','children'),
    [Input('dpd','value')]
)
def update(value):

    covid_data_30 = get_30_days_data(value)

    fig = go.Figure([
                go.Bar(
                    x = covid_data_30['date'].tail(30),
                    y = covid_data_30['confirmed new add'].tail(30),
                    name='Daily Confirmed Cases',
                    marker = {'color':'orange'},
                    hoverinfo='text',
                    hovertext=
                    '<b>Date</b>: ' + covid_data_30['date'].tail(30).astype(str)+'<br>' +
                    '<b>Daily Confirmed Cases</b>:' + [f'{i:.0f}' for i in covid_data_30['confirmed new add'].tail(30)]+'<br>' +
                    '<b>Country</b>: ' + covid_data_30['Country/Region'].tail(30).astype(str) + '<br>'
                ),
                go.Scatter(
                    x=covid_data_30['date'].tail(30),
                    y=covid_data_30['Rolling Ave.'].tail(30),
                    mode='lines',
                    name='Rolling Average of the last 7 days - Daily Confirmed Cases',
                    marker={'color': 'pink'},
                    hoverinfo='text',
                    hovertext=
                    '<b>Date</b>: ' + covid_data_30['date'].tail(30).astype(str) + '<br>' +
                    '<b>Rolling Ave.</b>:' + [f'{i:.0f}' for i in covid_data_30['Rolling Ave.'].tail(30)] + '<br>'
                )
            ]
    )
    fig.update_layout(
        paper_bgcolor='#182757',
        plot_bgcolor='#182757',
        legend={
            'orientation':'h',
            'xanchor':'center',
            'yanchor':'bottom',
            'x':0.5,
            'y':-0.25
            },
        margin=dict(
            t=25,
            b=0,
            l=0,
            r=5
        ),
        font=dict(
        # family="Lato",
        size=10,
        color="white"),
        height=400,
        yaxis={
                'title': '<b>Daily Confirmed Cases</b>',
                'color': 'black',
                'showline': True,
                'showgrid': True,
                'showticklabels': True,
                'linecolor': 'white',
                'linewidth': 1,
                'ticks': 'outside',
                'tickfont': {
                    'family': 'Aerial',
                    'color': 'white',
                    'size': 12
                }
            }
    )

    return [
        html.H6(f'Last 30 Days Confirmed Cases: {value}'),
        dcc.Graph(
            figure=fig,config={'displayModeBar': False}
        )
    ]


    