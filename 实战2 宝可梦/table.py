from dash import dash_table
import pandas as pd
import dash_bootstrap_components as dbc





def TableItem():
    df = pd.read_csv('实战2 宝可梦/data/pokemon.csv')
    return dash_table.DataTable(
                        id = 'table',
                        data=df.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df.columns],
                        page_size=15,
                        filter_action='native',
                        row_selectable='single'
                        )

