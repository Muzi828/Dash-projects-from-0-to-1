# from dash import Dash,html,Output,Input
# import dash_bootstrap_components as dbc


# app = Dash(__name__)


# def item(name,img_dir):
#     return dbc.ListGroupItem(
#         [html.H5(f"{name}: "),
#          html.Img(src=img_dir),
#          html.H5('--', id= name, className='float-right')
#          ]
#     )

# app.layout = dbc.Container(
#     [
#         # 单独放置在html中样式不会发生变化，需要放置在dbc组件中
#         # html.H1("汇率计算器-简单版"),
#         # html.P('write something here'),
#         # dbc.Input(value=0, id='ipt', type='number'),
#         dbc.ListGroup([
#                         dbc.ListGroupItem(children=[
#                             html.H1("汇率计算器-简单版"),
#                             html.P('write something here'),
#                             dbc.Input(value=0, id='ipt', type='number'),
#                         ],active='True'),
#         item('JPY', './assets/JPY.png'),
#         item('USD', './assets/USD.png'),
#         item('GBP', './assets/GBP.png'),
#             ],className='shadow')
#     ],style={'padding':'3rem'}
# )

# @app.callback(
#     [Output('JPY','children'),
#      Output('USD','children'),
#      Output('GBP','children')],
#     [Input('ipt','value')]
# )

# def update(value):
#     value = 0 if not value else value
#     return (
#         f'{value * 15.0} ￥',
#         f'{value * 0.14} $',
#         f'{value * 0.11} ￡'
#     )

# if __name__ == '__main__':
#     app.run_server(debug = True)


# #笔记：使用样式时候，需要是dbc的组件，而html是不行的，因此把html的部分替换一下




from dash import Dash,html,Output,Input
import dash_bootstrap_components as dbc

app = Dash()


def Item(name):
    return dbc.ListGroupItem(
                    [
                        html.H5(name),
                        html.Img(src=f'assets/{name}.png'),
                        html.H5('--',id=name, className='float-right')
                    ]
                )

item_ls = ['JPY','USD','GBP']

app.layout = dbc.Container(
    [
        dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        html.H1('汇率计算'),
                        html.P('write something here'),
                        dbc.Input(id='ipt',value=0, type='number'),
                    ],active ='True'
                )
            ]
        ),
           
        dbc.ListGroup(
            [Item(i) for i in item_ls],className='shadow'
        )
    ],style={'padding':'3rem'}
)


@app.callback(
    [Output('JPY','children'),Output('USD','children'),Output('GBP','children')],
    [Input('ipt','value')]
)
def update(value):
    value = 0 if not value else value
    return (value*2,value*3,value*4)

if __name__ == '__main__':
    app.run_server(debug=True)