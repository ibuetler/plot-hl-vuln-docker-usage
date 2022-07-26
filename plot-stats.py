#!/usr/bin/env python3
import pandas as pd
import plotly.express as px

df = pd.read_csv("trend.log")

fig = px.line(df, x = 'date', y = 'usage', title='Vulnerable Docker Status', render_mode='svg')
fig.show()
