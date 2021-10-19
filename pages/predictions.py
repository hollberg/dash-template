# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.
            
            ![Alt text](https://a3.espncdn.com/combiner/i?img=%2Fphoto%2F2021%2F1018%2Fr924485_1296x518_5%2D2.jpg&w=628&h=251&scale=crop&cquality=80&location=center&format=jpg "Los Bravos")

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])