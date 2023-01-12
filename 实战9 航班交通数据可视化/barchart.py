from dash import html,dcc,Input,Output
from app import app
import plotly.express as px
from api import state_airport_data


def BarchartInfo():
    return html.Div(
        [
            dcc.Graph('bar-chart')
        ]
    )

@app.callback(
    Output('bar-chart','figure'),
    [Input('dpd','value')]
)
def update(state):
    df = state_airport_data[state_airport_data['state']==state].groupby('airport')['cnt'].sum().reset_index()
    fig=px.bar(x=df.airport,y=df.cnt)
    fig.update_layout(
        paper_bgcolor = '#262626',
        plot_bgcolor = '#262626',
        xaxis=dict(title='<b></b>',
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linewidth=1,
                    zeroline=False,
                    ticks='outside',
                    tickfont=dict(
                        family='Aerial',
                        color='white',
                        size=12
                    )
                    ),
        yaxis=dict(title='<b></b>',
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linewidth=1,
                    zeroline=False,
                    gridcolor='gray',
                    ticks='outside',
                    tickfont=dict(
                        family='Aerial',
                        color='white',
                        size=12
                    )
            )
    )
    return fig