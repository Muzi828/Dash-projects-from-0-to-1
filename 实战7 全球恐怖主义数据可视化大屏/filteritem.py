from dash import html,dcc,Input,Output
from api import year_min,year_max,all_options
from app import app


def FilterInfo():
    return html.Div(
        [
            html.Div(
                [
                    html.H3('Select Region:',className='filter_item'),
                    dcc.Dropdown(
                        list(all_options.keys()),
                        'South Asia',
                        id='Region'
                    )
                ]
            ),
            html.Div(
                [
                    html.H3(f'Select Country:',className='filter_item'),
                    dcc.Dropdown(
                        id='Country'
                    )
                ],style={'paddingTop':'40px'}
            ),
            html.Div(
                [
                    html.H3('Select Year:',className='filter_item'),
                    dcc.RangeSlider(
                        min=year_min,
                        max=year_max,
                        step=1,
                        marks=None,
                        value=[2000,2010],
                        tooltip={"placement": "bottom", "always_visible": True},
                        id='Span-year'
                    )
                ],style={'paddingTop':'40px'}
            )
        ]
    )

@app.callback(
    Output('Country', 'options'),
    Input('Region', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('Country', 'value'),
    Input('Country', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']