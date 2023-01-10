from dash import Input,Output,dcc,html
from app import app
import plotly.graph_objects as go
from api import suicide_df

def Scatterchart():
    return html.Div(id = 'content')

@app.callback(
    Output('content','children'),
    [Input('dpd','value'),Input('rangeslider','value'),Input('checklist','value')]
)
def update(select_country, slider_year, radio_items):
    print(select_country, slider_year, radio_items)
    df = suicide_df[(suicide_df['country'] == select_country) & 
                        (suicide_df['year'] >= slider_year[0]) & 
                        (suicide_df['year'] <= slider_year[1]) & 
                        (suicide_df['age'].isin(radio_items))]
    
    fig = go.Figure(
        go.Scatter(
                    x=df['year'],
                    y=df['suicides_no'],
                    text = df['sex'],
                    textposition = 'top center',
                    mode = 'markers + text',
                    marker = dict(
                        size = df['suicides_no'] / 250,
                        color = df['suicides_no'],
                        colorscale = 'HSV',
                        showscale = False,
                        line = dict(
                            color = 'MediumPurple',
                            width = 2
                        )),
                    hoverinfo='text',
                    hovertext=
                    '<b>Country</b>: ' + df['country'].astype(str) + '<br>' +
                    '<b>Age</b>: ' + df['age'].astype(str) + '<br>' +
                    '<b>Sex</b>: ' + df['sex'].astype(str) + '<br>' +
                    '<b>Year</b>: ' + df['year'].astype(str) + '<br>' +
                    '<b>Population</b>: ' + [f'{x:,.0f}' for x in df['population']] + '<br>' +
                    '<b>Suicides/100k pop</b>: ' + [f'{x:,.0f}' for x in df['suicides/100k pop']] + '<br>' +
                    '<b>Suicides</b>: ' + [f'{x:,.0f}' for x in df['suicides_no']] + '<br>'
              )
    )
    fig.update_layout(
        paper_bgcolor='#202020',
        plot_bgcolor='#202020',
        font=dict(
        # family="Lato",
        size=14,
        color="white"),
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        xaxis=dict(title='<b>Year</b>',
                        color='white',
                        showline=True,
                        showgrid=False,
                        linecolor='white',
                        zeroline=False
                        
                ),

        yaxis=dict(
                title= '<b>Suicides</b>',
                color= 'white',
                showline= False,
                showgrid= True,
                gridcolor='#5a5a5a',
                tickfont={
                    'family': 'Aerial',
                    'color': 'white',
                    'size': 12
                },
                zeroline=False
        )
 
    )
    return [
            html.H3(f'Suicide Datas: {select_country}',style={'textAlign':'center'}),
            dcc.Graph(figure=fig,config={'displayModeBar': False})
        ]