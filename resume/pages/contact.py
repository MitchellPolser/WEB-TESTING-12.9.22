import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Mitchell Polser', className='mt-3'),
    dcc.Markdown('### Aspiring Security Professional', className='mb-5'),
    dcc.Markdown('### Personal info', style={'color':'gray'}),
    dcc.Markdown('Location', style=green_text),
    dcc.Markdown('Woodbridge, Virginia 22191'),
    dcc.Markdown('Phone Number', style=green_text),
    dcc.Markdown('571-409-0747'),
    dcc.Markdown('Email Address', style=green_text),
    dcc.Markdown('mitchellpolser@gmail.com'),
    dcc.Markdown('Linkedin', style=green_text),
    dcc.Markdown('www.linkedin.com', link_target='_blank'),
    dcc.Markdown('YouTube', style=green_text),
    dcc.Markdown('[www.youtube.com/charmingdata](https://www.youtube.com/charmingdata)', link_target='_blank'),
        ], width={'size':6, 'offset':2})
], justify='center')