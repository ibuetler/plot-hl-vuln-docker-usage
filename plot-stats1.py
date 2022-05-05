#!/usr/bin/env python3

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv('debug1.log')

    if n_clicks % 2 == 0:
        x, y = 'date', 'usage'
    else:
        x, y = 'date', 'usage'

    fig = px.line(df, x=x, y=y)    
    return fig


app.run_server(debug=True)
