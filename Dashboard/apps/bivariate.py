import pandas as pd
import dash
from dash.dependencies import Input,Output
from dash import html,dcc,dash_table,callback
from plotly import express as px
# pip install seaborn
import seaborn as sns
# pip install matplotlib
import matplotlib as plt
from plotly.subplots import make_subplots

dash.register_page(__name__,path='/bivariate',name="Bivariate Analysis",order=4)

df=pd.read_csv("dataset/adult_clean.csv") # data extracted from notebook after cleaning is read for the purpose of dashboard
num_features=['age','educational-num','capital-gain','capital-loss','hours-per-week']

layout=html.Div([
    html.H2("Bivariate Analysis"),
    html.H4("Cat Plot Visualization"),
    dcc.Dropdown(
        id='cat-x-dropdown',
        options=[
            {'label': 'Education', 'value': 'education'},
            {'label': 'Income Over 50k', 'value': 'income_over_50k'}
        ],
        value='education',  # Default value
        multi=False
    ),
    dcc.Graph(id='cat-plot'),
    html.Br(),
    html.H4("Group Bar Chart Visualization"),
    dcc.Dropdown(
        id='group-bar-x-dropdown',
        options=[
            {'label': 'Workclass', 'value': 'workclass'},
            {'label': 'Education', 'value': 'education'},
            {'label': 'Marital Status', 'value': 'marital-status'},
            {'label': 'Race', 'value': 'race'},
            {'label': 'Income Over 50k', 'value': 'income_over_50k'},
        ],
        value='education',  # Default value
        multi=False
    ),
    dcc.Dropdown(
        id='group-bar-color-dropdown',
        options=[
            {'label': 'Workclass', 'value': 'workclass'},
            {'label': 'Education', 'value': 'education'},
            {'label': 'Marital Status', 'value': 'marital-status'},
            {'label': 'Race', 'value': 'race'},
            {'label': 'Income Over 50k', 'value': 'income_over_50k'}
        ],
        value='income_over_50k',  # Default value
        multi=False
    ),
    dcc.Graph(id='group-bar-chart'),
    html.Br(),
    html.H4("Distribution of Numerical Features by Target Variable"),
    dcc.Dropdown(
        id='dist-feature-dropdown',
        options=[{'label': feature, 'value': feature} for feature in num_features],
        value=num_features[0],  # Default value
        multi=False
    ),
    dcc.Graph(id='distributions-plot'),
    html.Br(),
    html.H4("Scatter Plot Visualization"),
    dcc.Dropdown(
        id='scatter-x-dropdown',
        options=[
            {'label': 'Age', 'value': 'age'},
            {'label': 'Educational Number', 'value': 'educational-num'},
            {'label': 'Capital Gain', 'value': 'capital-gain'},
            {'label': 'Capital Loss', 'value': 'capital-loss'},
            {'label': 'Hours per Week', 'value': 'hours-per-week'}
        ],
        value='age',  # Default value
        multi=False
    ),
    dcc.Dropdown(
        id='scatter-y-dropdown',
        options=[
            {'label': 'Age', 'value': 'age'},
            {'label': 'Educational Number', 'value': 'educational-num'},
            {'label': 'Capital Gain', 'value': 'capital-gain'},
            {'label': 'Capital Loss', 'value': 'capital-loss'},
            {'label': 'Hours per Week', 'value': 'hours-per-week'}
        ],
        value='educational-num',  # Default value
        multi=False
    ),
    dcc.Graph(id='scatter-plot')
])


@callback(
    Output('cat-plot', 'figure'),
    [Input('cat-x-dropdown', 'value')]
)

def update_cat_plot(selected_x):
    fig1 = px.scatter(df, y='hours-per-week', x=selected_x, color=selected_x,
                     title=f'Cat Plot: {selected_x.title()} vs Working Hours')
    return fig1 



@callback(
    Output('group-bar-chart', 'figure'),
    [Input('group-bar-x-dropdown', 'value'),
     Input('group-bar-color-dropdown', 'value')]
)

def update_group_bar_chart(selected_x,selected_color):
    fig = px.histogram(df, x=selected_x, color=selected_color, barmode='group',
                       title=f'Group Bar Chart: {selected_x.title()} vs {selected_color.title()}')
    return fig



@callback(
    Output('distributions-plot', 'figure'),
    [Input('dist-feature-dropdown', 'value')],
)

def update_distribution_plot(selected_feature):
    fig_dist = px.histogram(df, x=selected_feature,color='income_over_50k', 
                            title=f'Distribution Plot - {selected_feature}',
                            labels={'income_over_50k': 'Income Over 50k'})
    return fig_dist



@callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-x-dropdown', 'value'),
     Input('scatter-y-dropdown', 'value')]
)

def update_scatter_plot(selected_x, selected_y):
    # Create scatter plot using plotly.express
    fig = px.scatter(df, x=selected_x, y=selected_y, color='income_over_50k',
                     title=f'Scatter Plot: {selected_x} vs {selected_y}', 
                     labels={'income_over_50k': 'Income Over 50k'})

    return fig