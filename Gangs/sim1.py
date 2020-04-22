#%%
import pandas as pd
import plotly.express as px


from classes.member import Namebase
from classes.gang import Gang
from classes.member import Member
from classes.racket import Racket
from classes.asset import Asset


# def main():
Gang('da dorfs')
Gang('da boiz')
day = 1
days = []
# strengths = pd.DataFrame()

# %%

for i in range(day, day+50):
    print(f'Day {i}')
    for gang_id in Gang.gang_dict:
        gang = Gang.gang_dict[gang_id]
        gang.activate()
day = i+1


# %%
for gang_id in Gang.gang_dict:
    gang = Gang.gang_dict[gang_id]
    strength = pd.DataFrame(gang.strength_log, columns=['Strength'])
    fig = px.line(strength, y="Strength", title=gang.name)
    fig.show()
# %%
