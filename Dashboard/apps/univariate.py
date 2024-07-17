import pandas as pd
import dash
from dash.dependencies import Input,Output
from dash import html,dcc,dash_table,callback
from plotly import express as px
#python -m pip install scipy
from scipy.stats import skew, kurtosis, jarque_bera

dash.register_page(__name__,path='/univariate',name="Univariate Analysis",order=3)

df=pd.read_csv("dataset/adult_clean.csv") # data extracted from notebook after cleaning is read for the purpose of dashboard
num_features=['age','educational-num','capital-gain','capital-loss','hours-per-week']
cat_features = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country','income_over_50k']

layout=html.Div([
    html.H2("Univariate Analysis"),
    html.H4("Numerical Features"),
    dcc.Dropdown(
        id='num-feature-dropdown',
        options=[{'label': feature, 'value': feature} for feature in num_features],
        value=num_features[0],  # Default value
        multi=False
    ),
    dcc.Graph(id='box-plot'),
    dcc.Graph(id='distribution-plot'),
    html.Div(id='num-feature-distribution'),
    html.Br(),
    html.H4("Categorical Features"),
    dcc.Dropdown(
        id='cat-treemap-dropdown',
        options=[{'label': feature, 'value': feature} for feature in cat_features],
        value=cat_features[0],  # Default value
        multi=False
    ),
    dcc.Graph(id='treemap-plot'),
    dcc.Dropdown(
        id='cat-pie-dropdown',
        options=[{'label': feature, 'value': feature} for feature in cat_features if feature != 'native-country'],  #since too many categories to accurately display in pie chart
        value=cat_features[0],  # Default value
        multi=False
    ),
    dcc.Graph(id='pie-chart')
])


@callback(
    [Output('box-plot', 'figure'),
     Output('distribution-plot', 'figure'),
     Output('num-feature-distribution', 'children')],
    [Input('num-feature-dropdown', 'value')]
)

def update_numeric_feature_plots(selected_feature):
    # Box Plot
    fig_box = px.box(df, y=selected_feature, title=f'Box Plot - {selected_feature}')

    # Distribution Plot
    fig_dist = px.histogram(df, x=selected_feature, title=f'Distribution Plot - {selected_feature}')

    # Skewness, Kurtosis, and JB Test
    skewness = skew(df[selected_feature])
    kurt = kurtosis(df[selected_feature])
    JB, p_val = jarque_bera(df[selected_feature])

    stats_text = f"**Skewness:** {skewness}\n"
    if skewness < 0:
        stats_text += "***Left Skewed***\n\n\n"
    elif skewness > 0:
        stats_text += "***Right Skewed***\n\n\n"
    else:
        stats_text += "***Center***\n\n\n"

    stats_text += f"**Kurtosis:** {kurt}\n"
    if kurt < 3:
        stats_text += "***Platykurtic***\n\n\n"
    elif kurt > 3:
        stats_text += "***Leptokurtic***\n\n\n"
    else:
        stats_text += "***Mesokurtic***\n\n\n"

    stats_text += f"**JB Test for Normality:**\n{JB}, {p_val}\n\n\n"
    if p_val < 0.05:
        stats_text += "**Distribution is not normal**\n"
    else:
        stats_text += "**Distribution is normal**\n"

    return fig_box, fig_dist, dcc.Markdown(stats_text)



@callback(
    Output('treemap-plot', 'figure'),
    [Input('cat-treemap-dropdown', 'value')]
)

def update_treemap(selected_feature):
    tempdf = pd.DataFrame(df[selected_feature].value_counts())
    tempdf['category'] = tempdf.index
    fig = px.treemap(tempdf, path=['category'], values='count', title=f'Tree Map of {selected_feature.title()}')
    return fig



@callback(
    Output('pie-chart', 'figure'),
    [Input('cat-pie-dropdown', 'value')]
)

def update_pie_chart(selected_feature):
    tempdf = pd.DataFrame(df[selected_feature].value_counts())
    tempdf['category'] = tempdf.index
    fig = px.pie(tempdf, values='count', names='category', title=f'Pie Chart of {selected_feature.title()}')
    return fig