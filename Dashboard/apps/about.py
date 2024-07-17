from dash import html
import dash

dash.register_page(__name__,path='/',name="About",order=0)

layout=html.Div(children=[
    html.Div(children=[
        html.H2("Adult Census Income Dataset Analysis"),
        "Dataset designed to predict whether income exceeds $50K/yr based on census data. Also known as Census Income dataset.",
        html.Br(),
        html.Br(),
        "Extraction was done by Barry Becker from the 1994 Census database.  A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)).",
        html.Br(),
        html.Br(),
        "Dataset type is Classification. Prediction task is to determine whether a person makes over 50K a year."
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Attribute Information"),
        html.B("Target Variable"),
        html.Br(),
        html.B("Income: "),">50K, <=50K",
        html.Br(),
        html.Br(),
        html.B("Features"),
        html.Br(),
        html.B("Age: "),"Continuous",
        html.Br(),
        html.B("Workclass: "),"Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked",
        html.Br(),
        html.B("Fnlwgt: "),"Continuous",
        html.Br(),
        html.B("Education: "),"Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool",
        html.Br(),
        html.B("Education-Num: "),"Continuous",
        html.Br(),
        html.B("Marital-Status: "),"Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse",
        html.Br(),
        html.B("Occupation: "),"Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces",
        html.Br(),
        html.B("Relationship: "),"Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried",
        html.Br(),
        html.B("Race: "),"White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black",
        html.Br(),
        html.B("Sex: "),"Female, Male",
        html.Br(),
        html.B("Capital-Gain: "),"Continuous",
        html.Br(),
        html.B("Capital-Loss: "),"Continuous",
        html.Br(),
        html.B("Hours-Per-Week: "),"Continuous",
        html.Br(),
        html.B("Native-Country: "),"United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands"
    ])
],className="bg-light p-4 m-2")