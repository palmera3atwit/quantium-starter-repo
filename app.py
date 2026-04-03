# Run this app with `python app.py` and visit http://127.0.0.1:8050/ in your web browser to see the result. 
# Make sure to run `python scripts/process_data.py` first to generate the necessary CSV file for this app.
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/pink_morsel_data.csv')

app.layout = html.Div(style={
    'backgroundColor': '#004c51',
    'minHeight': '100vh',
    'fontFamily': '"Helvetica Neue", monospace, sans-serif',
    'padding': '0',
}, children=[

    # Header
    html.Div(style={
        'background': 'linear-gradient(90deg, #004c51, #007075)',
        'padding': '24px 40px',
    }, children=[
        html.H1('Pink Morsel Sales Dashboard', style={
            'color': 'white',
            'margin': '0',
            'fontSize': '28px',
            'fontWeight': '700',
            'letterSpacing': '1px',
        }),
        html.P('Soul Foods — Regional Sales Performance', style={
            'color': 'rgba(255,255,255,0.75)',
            'margin': '6px 0 0 0',
            'fontSize': '14px',
        }),
    ]),

    # Controls
    html.Div(style={
        'padding': '28px 40px 0px',
        'display': 'flex',
        'alignItems': 'center',
        'gap': '20px',
    }, children=[
        html.Label('Filter by Region:', style={
            'color': 'white',
            'fontWeight': '600',
            'fontSize': '14px',
            'letterSpacing': '0.5px',
        }),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': ' All', 'value': 'all'},
                {'label': ' North', 'value': 'north'},
                {'label': ' East', 'value': 'east'},
                {'label': ' South', 'value': 'south'},
                {'label': ' West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'color': 'white', 'fontSize': '14px'},
            inputStyle={'marginRight': '5px', 'accentColor': 'white'},
            labelStyle={'marginRight': '20px', 'cursor': 'pointer', 'color': 'white'},
        ),
    ]),

    # Chart
    html.Div(style={'padding': '16px 40px 40px'}, children=[
        dcc.Graph(id='morsel-sales-graph')
    ]),
])


@callback(
    Output('morsel-sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered = df.groupby('date', as_index=False)['sales'].sum()
    else:
        filtered = df[df['region'] == selected_region].copy()

    fig = px.line(
        filtered,
        x='date',
        y='sales',
        title=f'Pink Morsel Sales — {"All Regions" if selected_region == "all" else selected_region.capitalize()}',
    )

    fig.update_traces(line=dict(color='#004c51', width=2.5))

    fig.update_layout(
        plot_bgcolor='#007075',
        paper_bgcolor='#007075',
        font=dict(color='#e0e0e0', family='"Helvetica Neue", monospace, sans-serif'),
        title=dict(font=dict(size=18, color='white')),
        xaxis=dict(
            title='Date',
            gridcolor='rgba(255,255,255,0.06)',
            linecolor='rgba(255,255,255,0.1)',
        ),
        yaxis=dict(
            title='Sales (USD)',
            gridcolor='rgba(255,255,255,0.06)',
            tickprefix='$',
        ),
        hovermode='x unified',
        margin=dict(l=60, r=30, t=50, b=60),
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)