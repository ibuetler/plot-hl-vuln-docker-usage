#!/usr/bin/env python3
import pandas as pd
import plotly.express as px
import argparse, os

<<<<<<< HEAD
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="path to the source log file", required=True)
args = parser.parse_args()

# check if source log file exists
if not os.path.exists(args.file):
    print(args.file + " not found")
    exit(1)


df = pd.read_csv(args.file)
=======
df = pd.read_csv("trend.log")
>>>>>>> ad5b1f8c045c9339c71f6423f9140eb486bee029

fig = px.line(df, x = 'date', y = 'usage', title='Vulnerable Docker Status', render_mode='svg')
fig.show()
