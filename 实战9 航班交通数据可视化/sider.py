from dash import html,dcc
from api import state_ls,max_airport



def SiderInfo():
    return html.Div(
        [
            html.H3('Airport Traffic Data'),
            html.H6('Select State'),
            dcc.Dropdown(
                state_ls,
                max_airport,
                id='dpd'
            )
        ]
    )













# def SiderInfo():
#     return html.Div(
#         [
#             html.H3('Airport Traffic Data',style={'paddingBottom':'50px'}),
#             html.H6('Select State',style={'paddingBottom':'50px'}),
#             dcc.Dropdown(
#                 state_ls,
#                 state_ls[0],
#                 id='dpd'
#             )
#         ]
#     )
