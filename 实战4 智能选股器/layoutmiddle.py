from dash import html,dcc,Input,Output,dash_table
import dash_bootstrap_components as dbc
from api import add_fields
from app import app

def TableInfo():
    
    return dbc.Container(
        [
            dash_table.DataTable(
                data = None,
                id = 'table'
            )
        ]
    )

@app.callback(
    Output('table','data'),
    [Input('dpd','value'),Input('换手率','value'),Input('量比','value')]
)
def update(v1,v2,v3):
    df = add_fields(v1)
    df = df[(df['量比']>v2[0]) & (df['量比']<v2[1]) & (df['换手率']>v3[0]) & (df['换手率']<v3[1])]
    
    df = df[['ts_code','name','area','换手率','量比']]
    df.columns = ['股票代码','股票名称','发行区域','换手率','量比']

    return df.to_dict('records')
