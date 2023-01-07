
import dash
from dash import html


app = dash.Dash()


my_list = ["🍎"+"APPLE",
    "🍌"+"BANANA",
    "🥭"+"MONGO",
    "🍇"+"GRAPES",
    "🍐"+"PEAR"]

app.layout = html.Ul([
    html.Li(i) for i in my_list
])


if __name__ == '__main__':
    app.run_server(debug=True)