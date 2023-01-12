from dash import html,dash_table,Input,Output,dcc
import dash_bootstrap_components as dbc
from app import app
from api import get_data
import plotly.express as px
from middle import update_layout
import plotly.graph_objects as go

def BottomInfo():
    return dbc.Row(
        [
            dbc.Col([SaleTable()],width=4,className='card_container'),
            dbc.Col([State_or_City()],width=3,className='card_container'),
            dbc.Col([State_and_City()],className='card_container'),
        ]
    )


#以下是第一部分的内容设置
def SaleTable():
    return dash_table.DataTable(id='table-sale',
                         page_size=20,
                         virtualization=True,
                         style_cell={'textAlign': 'left',
                                     'min-width': '100px',
                                     'backgroundColor': '#1f2c56',
                                     'color': '#FEFEFE',
                                     'border-bottom': '0.01rem solid #19AAE1'},
                         style_header={'backgroundColor': '#1f2c56',
                                       'fontWeight': 'bold',
                                       'font': 'Lato, sans-serif',
                                       'color': 'orange',
                                       'border': '#1f2c56'},
                         fixed_rows={'headers': True},
                         sort_action='native',
                         sort_mode='multi',
                    )

@app.callback(
    Output('table-sale','data'),
    [Input('slider-year','value'),Input('radio-segment','value')]
)
def update(year,segment):
    df = get_data(year,segment)
    filter_df = df[['Order Date', 'Customer ID', 'Customer Name','Segment', 'City', 'State', 'Region','Category', 'Sub-Category', 'Product Name','Sales', 'year', 'month']]
    return filter_df.to_dict('records')

#以下是第二部分的内容设置
def State_or_City():
    return html.Div(
        [
            dcc.RadioItems(['State','City'],'State',id='radio-state-or-city'),
            dcc.Graph(id='bar-state-or-city')
        ]
    )
@app.callback(
    Output('bar-state-or-city','figure'),
    [Input('slider-year','value'),Input('radio-segment','value'),Input('radio-state-or-city','value')]
)
def update(year,segment,state_or_city):
    df = get_data(year,segment)
    sales_data_series = df.groupby(state_or_city)['Sales'].sum().sort_values(ascending=False)[:5][::-1]
    fig = px.bar(x=sales_data_series.values,y=sales_data_series.index,orientation='h',text=sales_data_series.values)
    fig.update_traces(texttemplate='$' + '%{text:,.2s}', textposition='inside')
    fig.update_layout(height=520)
    return update_layout(fig,state_or_city,year)


#以下是第三部分的内容设置
def State_and_City():
    return dcc.Graph(id='scatter-state-and-city')

@app.callback(
    Output('scatter-state-and-city','figure'),
    [Input('slider-year','value'),Input('radio-segment','value')]
)
def update(year,segment):
    df = get_data(year,segment)   
    obtain_fields = ['year', 'month', 'Segment', 'State', 'City']
    sales_data_df = df.groupby(obtain_fields)['Sales'].sum().reset_index()
    fig = go.Figure(
            go.Scatter(
                    x=sales_data_df['month'],
                    y=sales_data_df['Sales'],
                    mode='markers',
                    line=dict(width=3, color='orange'),
                    marker=dict(color= sales_data_df['Sales'],
                                colorscale = 'HSV',
                                showscale = False,
                                size=sales_data_df['Sales'] / 250,
                                symbol='circle',
                                line=dict(color='MediumPurple', width=2)),
                    hoverinfo='text',
                    hovertext=
                    '<b>Year</b>: ' + sales_data_df['year'].astype(str) + '<br>' +
                    '<b>Month</b>: ' + sales_data_df['month'].astype(str) + '<br>' +
                    '<b>Segment</b>: ' + sales_data_df['Segment'].astype(str) + '<br>' +
                    '<b>State</b>: ' + sales_data_df['State'].astype(str) + '<br>' +
                    '<b>City</b>: ' + sales_data_df['City'].astype(str) + '<br>' +
                    '<b>Sales</b>: $' + [f'{x:,.0f}' for x in sales_data_df['Sales']] + '<br>'

                )
        )
    fig.update_layout(height=550)
    return update_layout(fig,'State and City',year)