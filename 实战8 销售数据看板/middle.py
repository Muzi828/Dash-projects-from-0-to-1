from dash import html,dcc,Input,Output
import dash_bootstrap_components as dbc
from app import app
from api import get_data,year_ls,data
import plotly.express as px
import plotly.graph_objects as go

def MiddleInfo():
    return dbc.Row(
        [
            dbc.Col([Sub_Category_or_Region()],className='card_container',width=3),
            dbc.Col([CategoryPie()],className='card_container',width=3),
            dbc.Col([MonthLine()],className='card_container',width=4),
            dbc.Col([YOY()],className='card_container')
        ]
    )

##以下是共用的部分
def update_layout(fig,type_,year):
    fig.update_layout(
        paper_bgcolor='#1f2c56',
        plot_bgcolor='#1f2c56',
        titlefont={'color': 'white',
                       'size': 15},
        font=dict(family='sans-serif',
                    color='white',
                    size=15),
        legend={'orientation': 'h',
                'bgcolor': '#010915',
                'xanchor': 'center', 'x': 0.5, 'y': -0.2},
        margin=dict(t=50,r=20,l=0,b=0),
        title={'text': f'Sales by {type_} {year}',
                   'y': 0.99,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
        xaxis=dict(title='<b></b>',
                    color = 'orange',
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='orange',
                    linewidth=1,
                    zeroline=False,
                    ticks='outside',
                    tickfont=dict(
                        family='Aerial',
                        color='orange',
                        size=12
                    )),
        yaxis=dict(title='<b></b>',
                    color='orange',
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='orange',
                    linewidth=1,
                    zeroline=False,
                    gridcolor='gray',
                    ticks='outside',
                    tickfont=dict(
                        family='Aerial',
                        color='orange',
                        size=12
            )
        )
    )
    return fig



##以下是第一个图形中的内容设置
def Sub_Category_or_Region():
    return html.Div(
        [
            dcc.RadioItems(
                ['Sub-Category','Region'],
                'Sub-Category',
                id = 'radio-sub-category-or-region'
            ),
            dcc.Graph(id='h-bar-sub-category-or-region')
        ]
    )

@app.callback(
    Output('h-bar-sub-category-or-region','figure'),
    [Input('slider-year','value'),Input('radio-segment','value'),Input('radio-sub-category-or-region','value')]
)
def update(year,segment,sub_category_or_region):
    df = get_data(year,segment)
    sales_data_series = df.groupby(sub_category_or_region)['Sales'].sum().sort_values(ascending=False)[:5][::-1]
    fig = px.bar(x=sales_data_series.values,y=sales_data_series.index,orientation='h',text=sales_data_series)
    fig.update_layout(height=400)
    fig.update_traces(texttemplate='$' + '%{text:,.2s}', textposition='inside')
    return update_layout(fig,sub_category_or_region,year)


##以下是第二个图形内容设置
def CategoryPie():
    return dcc.Graph(id='pie-category')

@app.callback(
    Output('pie-category','figure'),
    [Input('slider-year','value'),Input('radio-segment','value')]
)
def update(year,segment):
    df = get_data(year,segment)
    type_ = 'Category'
    sales_data_series = df.groupby(type_)['Sales'].sum()
    fig=px.pie(values=sales_data_series.values,names=sales_data_series.index,hole=.7)
    # fig.update_layout(height=400)
    return update_layout(fig,type_,year)


##以下是第三个图形的内容设置
def MonthLine():
    return dcc.Graph(id='line-month')

@app.callback(
    Output('line-month','figure'),
    [Input('slider-year','value'),Input('radio-segment','value')]
)
def update(year,segment):
    df = get_data(year,segment)
    type_='month'
    sales_data_series = df.groupby(type_)['Sales'].sum()
    fig = go.Figure(go.Scatter(
                x=sales_data_series.index,
                y=sales_data_series.values,
                text = sales_data_series.values,
                texttemplate= '$' + '%{text:,.2s}',
                textposition='bottom left',
                mode='markers+lines+text',
                line=dict(width=3, color='orange'),
                marker=dict(color='#19AAE1', size=10, symbol='circle',
                            line=dict(color='#19AAE1', width=2))
            ))
    return update_layout(fig,type_,year)


##以下是第四部分的内容设置
def YOY():
    return html.Div(id='YOY')

@app.callback(
     Output('YOY','children'),
    [Input('slider-year','value')]
)
def update(year):
    current_year_sales=data[data['year']==year]['Sales'].sum()
    if year != min(year_ls):
        previous_year_sales=data[data['year']==year-1]['Sales'].sum()
        yoy_growth=(current_year_sales-previous_year_sales)*100/previous_year_sales
    else:
        previous_year_sales='No data'
        yoy_growth='No data'
    return [
        html.H6('Current Year'),
        html.P(f'${current_year_sales:,.0f}',className='year_sale'),
        html.H6('Previous Year'),
        html.P(f'${previous_year_sales:,.0f}',className='year_sale'),
        html.H6('YOY Grouth'),
        html.P(f'{yoy_growth:.2f}%',className='year_sale'),
    ]

