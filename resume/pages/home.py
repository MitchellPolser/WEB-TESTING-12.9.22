import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    dcc.Markdown('# Mitchell L. Polser', style={'textAlign':'center'}),
    dcc.Markdown('Woodbridge, VA', style={'textAlign': 'center'}),

    html.Hr(style={'borderColor' : 'white', 'color' : 'rgb(32,55,76)', 'opacity' : '150', 'height' : '3px', 'width' : '70%', 'marginLeft': 'auto', 'marginRight' : 'auto',}),
    dcc.Markdown('Aspiring information security professional, currently studying at the George Washington University. \n'
                 'I have a passion for all things technology, with a particular interest in cybersecurity, machine learning, \n'
                 'as well as data analytics/visualization.',
                 style={'textAlign': 'center', 'white-space': 'pre'}),
    html.Hr(style={'color' : 'rgb(32,55,76)', 'opacity' : '150', 'height' : '3px'}),
    dcc.Markdown('### Industry Certifications', style={'textAlign': 'center'}),
    html.Hr(style={'color' : 'white',  'width': '23%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-5px'}),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * CompTIA Security+ 
            ''')
            
            ### EXTRA BULLETS
            #* Inventory control procedures
            #* Merchandising expertise
            #''')
            ### EXTRA BULLETS END
            
        ], width={"size": 3, "offset": 0}),
        dbc.Col([
            dcc.Markdown('''
            * CompTIA Network+ 
            ''')
        ], width=3)
    ], justify='center'),
    html.Hr(style={'color' : 'rgb(32,55,76)', 'opacity': '150', 'height' : '3px'}),
     dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(style={'width': '12%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-5px'}),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('2021-2023',
                         style={'textAlign': 'center'}),
            
            html.Hr(style={'color' : 'white', 'width': '47%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-15px'}),
            
        ], width=2),
        dbc.Col([
            dcc.Markdown('Bachelor of Professional Studies in Cybersecurity\n'
                         'The George Washington University - Washington, D.C.',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5),
        html.Hr(style={'width': '50%', 'marginLeft': 'auto', 'marginRight' : 'auto'})
    ], justify='center',),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('2019-2021',
                         style={'textAlign': 'center',}),
            
            html.Hr(style={'color' : 'white', 'width': '47%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-15px'}),
            
        ], width=2),
        dbc.Col([
            dcc.Markdown('Applied Associate of Science in Cybersecurity\n'
                         'Northern Virginia Community College - Woodbridge, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    
    html.Hr(style={'color' : 'rgb(32,55,76)', 'opacity' : '150', 'height' : '3px'}),
    dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    html.Hr(style={'width': '16%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-5px',}),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('Oct. 2021 - Nov. 2021',
                         style={'textAlign': 'center'}),
            
            html.Hr(style={'color' : 'white', 'width': '88%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-15px'}),
                
        ], width=2),
        dbc.Col([
            dcc.Markdown('Service Desk Technician \n'
                         'Armed Forces Benefit Association - Alexandria, VA',
                         style={'white-space': 'pre',},
                         className='ms-3'),
            
            html.Ul([
                html.Li(
                    'Performed internal end user support for all organizational IT resources'),
                html.Li(
                    'Managed organization users and computers through Active Directory'),
            ])
        ], width=5)
    ], justify='center'),
    html.Hr(style={'width': '65%', 'marginLeft': 'auto', 'marginRight' : 'auto'}),
    
     dbc.Row([
        dbc.Col([
            dcc.Markdown('June 2019 - Nov. 2020',
                         style={'textAlign': 'center',}),
            
            html.Hr(style={'color' : 'white', 'width': '88%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-15px'}),
            
        ], width=2),
        dbc.Col([
            dcc.Markdown('Associate \n'
                         'Tech Time Gaming Lounge - Woodbridge, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    "Assisted customers in confiurging peripheral gaming devices to PC's"),
                html.Li(
                    'Performed hardware/software troubleshooting'),
            ])
        ], width=5)
    ], justify='center'),
     html.Hr(style={'width': '65%', 'marginLeft': 'auto', 'marginRight' : 'auto'}),
     
     dbc.Row([
        dbc.Col([
            dcc.Markdown('Jan. 2019 - Present', style={'textAlign': 'center'}),
            
            html.Hr(style={'color' : 'white', 'width': '88%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-15px'}),
        
        ], width=2),
        dbc.Col([
            dcc.Markdown('Delivery Driver \n'
                         'Doordash - Woodbridge, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('3800+ food deliveries completed'),
                html.Li('5/5 customer devlivery rating'),
            ])
        ], width=5)
    ], justify='center'),
     html.Hr(style={'width': '65%', 'marginLeft': 'auto', 'marginRight' : 'auto'}),
     
      dbc.Row([
        dbc.Col([
            dcc.Markdown('May 2017 - June 2019',
                         style={'textAlign': 'center'}),
            
            html.Hr(style={'color' : 'white', 'width': '88%', 'marginLeft': 'auto', 'marginRight' : 'auto', 'marginTop' : '-15px'}),
        ], width=2),
        dbc.Col([
            dcc.Markdown('Shift Manager \n'
                         'Escape Room Woodbridge - Woodbridge, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Delegated operational responsibilities to staff'),
                html.Li(
                    'Managed customer satisfaction'),
            ])
        ], width=5)
    ], justify='center')
      
      
   

], style= {'borderStyle': 'solid', 'borderColor': 'rgb(32,55,76)' , 'width' : '70%', 'margin' : 'auto', 'marginTop' : '1em', 'marginBottom' : '1em'})
