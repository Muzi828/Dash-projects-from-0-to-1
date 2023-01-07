import dash

from dash import html  #第一个核心组件：网页(其中两个重要部分组成，children和style)

app = dash.Dash(__name__)# app的名称

block = html.Div(
    [
        html.H1('Use DASH write all stuff!',
                style={'fontSize':'6rem','color':'white'}),
        html.Img(src='assets/meme.png')
    ],style={'textAlign':'center'})
app.layout = block

if __name__ == '__main__':
    app.run_server(debug = True)