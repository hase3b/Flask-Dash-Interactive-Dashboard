import pandas as pd
import dash
from dash import html,dcc,dash_table

dash.register_page(__name__,path='/dataset',name="Dataset",order=1)

df=pd.read_csv("dataset/adult_clean.csv") # data extracted from notebook after cleaning is read for the purpose of dashboard 

layout=html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=df.to_dict("records"),
                         page_size=20,
                         style_cell={'textAlign': 'left','padding': '10px','background-color': '#f4f4f4'},
                         style_header={'background-color': 'grey','fontWeight': 'bold','color': 'white','border': '1px solid #dee2e6'}                                
    )
],style={'width': '100%', 'overflowX':'auto'})