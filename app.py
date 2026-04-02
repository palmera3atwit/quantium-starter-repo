# Run this app with `python app.py` and visit http://127.0.0.1:8050/ in your web browser to see the result. 
# Make sure to run `python scripts/process_data.py` first to generate the necessary CSV file for this app.
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/pink_morsel_data.csv')

fig = px.line(df, x="date", y="sales",title='Pink Morsel Sales Over Time by Region')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Dashboard'),

    html.Div(children='''
        Pink Morsel Sales Data Visualization
    '''),

    dcc.Graph(
        id='morsel-sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
