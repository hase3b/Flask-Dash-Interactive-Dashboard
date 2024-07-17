import pandas as pd
import dash
from dash.dependencies import Input,Output
from dash import html,dcc,dash_table,callback

dash.register_page(__name__,path='/descriptive',name="Descriptive Statistics",order=2)

df=pd.read_csv("dataset/adult_clean.csv") # data extracted from notebook after cleaning is read for the purpose of dashboard
cat_features=['workclass','education','marital-status', 'occupation', 'relationship', 'race', 'gender','native-country']

layout=html.Div([
    html.H2("Descriptive Statistics"),
    html.H4("Class Balance"),
    dash_table.DataTable(data=pd.DataFrame(df['income_over_50k'].value_counts(normalize=True).reset_index()).rename(columns = {'index':'category'}).to_dict("records"),
                         page_size=20,
                         style_cell={'textAlign': 'left','padding': '10px','background-color': '#f4f4f4'},
                         style_header={'background-color': 'grey','fontWeight': 'bold','color': 'white','border': '1px solid #dee2e6'}                                
    ),
    html.Br(),
    html.H4("Descriptive Statistics - Numeric Variables"),
    dash_table.DataTable(data=df.describe().to_dict("records"),
                         page_size=20,
                         style_cell={'textAlign': 'left','padding': '10px','background-color': '#f4f4f4'},
                         style_header={'background-color': 'grey','fontWeight': 'bold','color': 'white','border': '1px solid #dee2e6'}                                
    ),
    html.Br(),
    html.H4("Descriptive Statistics - Categorical Features"),
    dash_table.DataTable(data=df.describe(include='object').to_dict("records"),
                         page_size=20,
                         style_cell={'textAlign': 'left','padding': '10px','background-color': '#f4f4f4'},
                         style_header={'background-color': 'grey','fontWeight': 'bold','color': 'white','border': '1px solid #dee2e6'}                                
    ),
    html.Br(),
    html.H4("Categorical Features Distribution"),
    dcc.Dropdown(
        id='cat-feature-dropdown',
        options=[{'label': feature, 'value': feature} for feature in cat_features],
        value=cat_features[0],  # Default value
        multi=False
    ),
    html.Div(id='cat-feature-distribution')
])

@callback(
    Output('cat-feature-distribution', 'children'),
    [Input('cat-feature-dropdown', 'value')]
)
def update_cat_feature_distribution(selected_feature):
    distribution = df[selected_feature].value_counts(normalize=True)
    return dash_table.DataTable(data=pd.DataFrame(df[selected_feature].value_counts().reset_index()).rename(columns = {'index':'category'}).to_dict("records"),
                         page_size=20,
                         style_cell={'textAlign': 'left','padding': '10px','background-color': '#f4f4f4'},
                         style_header={'background-color': 'grey','fontWeight': 'bold','color': 'white','border': '1px solid #dee2e6'}                                
    )