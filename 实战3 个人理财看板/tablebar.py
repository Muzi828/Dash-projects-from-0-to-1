
from dash import Dash,html,Output,Input,dcc
import dash_bootstrap_components as dbc
import pandas as pd
from dash import  dash_table
from app import app
import os 



def TableItem():

    df = pd.read_excel('实战3 个人理财看板/data/1月账单.xlsx')
    return html.Div(
        [   
            dcc.Dropdown(
                id = 'dpd',
                options = [{'label':i[:-5],'value':i} for i in os.listdir('实战3 个人理财看板/data/')],
                value = '1月账单.xlsx'
            ),
            dash_table.DataTable(
                    id= 'table',
                    data =df.to_dict('records'),
                    columns = [{'id':i,'name':i} for i in df.columns],
                    page_size=10,
                    )
        ]
    )


@app.callback(Output('table','data'),[Input('dpd','value')])
def update(v):
    return pd.read_excel(f'实战3 个人理财看板/data/{v}').to_dict('records')

