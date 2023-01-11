from dash import html,dcc,Input,Output
from app import app
import plotly.express as px
from api import geo_df

def MapInfo():
    return html.Div(
        [
            dcc.Graph(id='map')
        ]
    )

@app.callback(
    Output('map','figure'),
    [Input('Region','value'),Input('Country','value'),Input('Span-year','value')]
)
def update(region,country,span_year):

    geo_df_filter = geo_df[
        (geo_df['region_txt']==region) & (geo_df['country_txt']==country) & (geo_df['iyear']>=span_year[0]) & (geo_df['iyear']<=span_year[1])
    ]

    fig = px.scatter_mapbox(geo_df_filter, lat="latitude", lon="longitude", color="nkill", size="attacktype1",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,zoom=2,
                   hover_data = geo_df_filter.columns)

    fig.update_layout(
        font = {'family':'sans-serif','color':'white','size':12},
        paper_bgcolor = '#070707',
        plot_bgcolor = '#070707',
        margin=dict(r=0, l =0, b = 0, t = 0),
        mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',
                style='dark',
            ),
    )
    return fig