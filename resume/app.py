import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SUPERHERO])

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"), 
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"], class_name="me-auto")
                        for page in dash.page_registry.values()
                        if not page["path"].startswith("/app")
                        ], class_name = 'mr-auto', justified = 'true'),
            ], class_name='flex-grow-1')
        ],
        fluid=True,
    ),
    dark=True,
    color='dark',
)

app.layout = dbc.Container([header, dash.page_container], fluid=False)

if __name__ == '__main__':
	app.run_server()