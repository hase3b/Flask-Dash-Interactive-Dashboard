from dash import html,dcc
import dash
#pip install dash-bootstrap-components
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import pandas as pd
import numpy as np

app=dash.Dash(use_pages=True,pages_folder='apps',external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([
    html.Br(),
    html.Img(src='/assets/logo.png',className="mx-auto d-block"),
    html.Br(),
    html.P("Adult Census Income Analytical Dashboard",className="h1 text-center text-dark fw-bold"),
    html.Hr(),
    html.Div(children=[
        dcc.Link(page['name'],href=page['relative_path'],className="btn btn-secondary m-2 btn-lg")\
            for page in dash.page_registry.values()],
    className="text-center"),
    dash.page_container,
    html.Br()
],className='container')



if __name__=='__main__':
    app.run(debug=True)