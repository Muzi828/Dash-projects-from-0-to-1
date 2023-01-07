
import dash
from dash import html,dcc,Input,Output


app = dash.Dash()


textaera = dcc.Textarea(value='',id='text',style={'width':'95%','height':'10rem'})
markdown = dcc.Markdown('',id='mk')
app.layout = html.Ul(
    [
        markdown,
        html.H3('输入文字'),
        html.Hr(),
        textaera
    ]
)

@app.callback(
    Output(component_id='mk',component_property='children'),
    [Input(component_id='text',component_property='value')]  
)
def update(v):
    return v


if __name__ == '__main__':
    app.run_server(debug=True)