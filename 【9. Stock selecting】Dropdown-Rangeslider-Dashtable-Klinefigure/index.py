from dash import html
import dash_bootstrap_components as dbc
from app import app


from layoutleft import DropDownInfo,RangeSliderInfo
from layoutmiddle import TableInfo
from layoutright import FigureInfo

app.layout = dbc.Row(
    [
        dbc.Col([DropDownInfo(),RangeSliderInfo()],width=2,className='vh-100 border-right border-dark sider'),
        dbc.Col([TableInfo()],width=5,className='py-2'),
        dbc.Col([FigureInfo()]),
    ]
)

if __name__ == '__main__':
    app.run_server(debug = True)