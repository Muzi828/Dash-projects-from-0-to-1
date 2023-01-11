from dash import html
from dash import html,dcc,Input,Output
from app import app
import plotly.graph_objects as go
from api import get_data



def StackBarLineInfo():
    return html.Div(
        [
            html.Div(id='stack-content')
        ]
    )

@app.callback(
    Output('stack-content','children'),
    [Input('Region','value'),Input('Country','value'),Input('Span-year','value')]
)
def update(region,country,span_year):

    death,injured,attack = get_data(region,country,span_year)
    span_year_ls = list(range(span_year[0],span_year[1]+1))

    fig = go.Figure(
        [
            go.Bar(x=span_year_ls,y=death,name='Death'),
            go.Bar(x=span_year_ls,y=injured,name='Injured'),
            go.Scatter(mode='markers + lines',x=span_year_ls,y=attack,name='Attack')
        ]
    )
    fig.update_layout(
            barmode = 'stack',
            titlefont = {'color':'white','size':20},
            font = {'family':'sans-serif','color':'white','size':12},
            hovermode = 'closest',
            paper_bgcolor = '#070707',
            plot_bgcolor = '#070707',
            legend = {'orientation':'h','bgcolor':'#070707','xanchor':'center','x': 0.5, 'y': -0.2},
            margin = {'r':0,'l':60,'b':100,'t':20},

            xaxis = {'title':'<b>Year</b>','color':'white','showline':True,'showgrid':True,'tick0':0,'dtick':1,'gridcolor':'#010915',
                    'showticklabels':True,'linecolor':'white','linewidth':1,'ticks':'outside','tickfont':{'family':'sans-serif','color':'white','size':12}
                    },
            yaxis = {'title':'<b>Death</b>','color':'white','showline':True,'showgrid':True,'gridcolor':'#010915',
                    'showticklabels':True,'linecolor':'white','linewidth':1,'ticks':'outside','tickfont':{'family':'sans-serif','color':'white','size':12}
                    }
    )
    return [
        html.H3(f'Death,Injured and Attack: {country}'),
        dcc.Graph(figure=fig)
    ]
