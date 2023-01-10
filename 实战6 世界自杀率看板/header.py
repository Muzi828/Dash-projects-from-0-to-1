
from dash import html

def HeaderInfo():
    return html.Div(
        [
            html.H1('World Suicides Data',style={'textAlign':'center','paddingBottom':'20px'})
        ]
    )