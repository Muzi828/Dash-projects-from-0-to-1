from dash import html

def SideBar():
    return html.Div(
        [
            html.Img(src = 'assets/shocked.jpg',
            height='200px',
            width='200px',className='rounded-circle'),
            html.H5('Good Morning',style={'color':'white','padding':'3rem'})
        ],style={'textAlign':'center'},className='mt-4'
    )