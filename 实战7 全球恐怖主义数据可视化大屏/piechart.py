from dash import html,dcc,Input,Output
from app import app
import plotly.graph_objects as go
from api import get_data
import plotly.express as px

def PieInfo():
    return html.Div(id='pie_content')

@app.callback(
    Output('pie_content','children'),
    [Input('Region','value'),Input('Country','value'),Input('Span-year','value')]
)
def update(region,country,span_year):
    data = get_data(region,country,span_year)

    fig = px.pie(values=[sum(i) for i in data],names=['deanth','injured','attack'],hole=0.65)

    fig.update_layout(
        paper_bgcolor = '#070707',
        plot_bgcolor = '#070707',
        font = {'family':'sans-serif','color':'white','size':12},
        legend = {'orientation':'h','bgcolor':'#070707','xanchor':'center','x': 0.5, 'y': -0.2},
    )

    return [
        html.H3(f'Death,Injured and Attack: {country}'),
        dcc.Graph(figure=fig)
    ]