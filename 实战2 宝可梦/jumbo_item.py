import dash_bootstrap_components as dbc
from dash import dcc,html
import plotly.express as px

def JumboItem(name,tags,albs):
    
    hex_area = {
        "r":albs,
        "theta": ["HP", "Attack", "Defense", "Sp.Attack", "Sp.Defense", "Speed"],
    }

    fig = px.line_polar(hex_area, r='r', theta='theta', line_close=True,range_r=[0,255],width=350,height=350)

    return [dbc.Row(
        [
            dbc.Col([
                html.Img(
                    src=f"https://img.pokemondb.net/artwork/large/{name.lower()}.jpg",
                    height = '200px',
                    width = '200px'
                ),
                html.H1(name.upper()),
                html.Span([dbc.Badge(i, color="primary", className="mr-1") for i in tags])

            ]),
            dbc.Col([
                dcc.Graph(figure= fig)
            ])
        ],style= {'textAlign':'center'}
    )]