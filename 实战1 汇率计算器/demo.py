

from dash import Dash,html,dcc,Input,Output
import dash_bootstrap_components as dbc


app = Dash()

app.layout = dbc.Container(
    [
        dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        html.H5('这是左边',className='float-left'),
                        html.H5('这是右边',className='float-right'),
                    ]
                )
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)

    #测试发现是和加载的css样式有关系