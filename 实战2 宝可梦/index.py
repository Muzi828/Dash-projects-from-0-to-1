


from dash import Dash,Output,Input,html
import pandas as pd
import dash_bootstrap_components as dbc


from table import TableItem
from jumbo_item import JumboItem

app = Dash()

df = pd.read_csv(r'实战2 宝可梦/data/pokemon.csv')

app.layout = html.Div(
    [
        dbc.Container('',id= 'target'),
        dbc.Container([TableItem()],className='shadow')
    ],style = {'padding':'3rem'}
)

@app.callback(
    [Output('target','children')],
    [Input('table','selected_rows')]
)
def update(selected_rows):
    row_num = 0 if not selected_rows else selected_rows[0]
    contents = df.loc[row_num].to_list()
    
    name = contents[1]
    tags = contents[2:4]
    albs = contents[5:11]

    print(name,tags,albs)
    return JumboItem(name,tags,albs)
    
    

if __name__ == '__main__':
    app.run_server(debug=True)