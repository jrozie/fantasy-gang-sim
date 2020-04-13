#%%
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
import random


from classes.member import Namebase
from classes.gang import Gang
from classes.member import Member
from classes.racket import Racket
from classes.asset import Asset


# def main():
#gang1 = Gang('da dorfs')

# %%
strength_list = []
training_skill = 60


# %%


#%%

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Graph(id='gang_strength'),
    dcc.Input(id='training_skill', value=60, type='number')
])

@app.callback(
    Output('gang_strength', 'figure'),
    [Input('training_skill', 'value')])
def update_figure(value):
    gang1 = Gang('da dorfs')
    strength_list = []
    for i in range(0,200):
        if value > random.randrange(0,100):
            gang1.train()
        strength_list.append(gang1.get_strength())

    strength = pd.DataFrame(strength_list, columns=['Strength'])

    df = strength
    fig = px.line(strength, y="Strength")
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)