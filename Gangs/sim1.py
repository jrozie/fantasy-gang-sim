#%%
import pandas as pd
import plotly.express as px


from classes.member import Namebase
from classes.gang import Gang
from classes.member import Member
from classes.racket import Racket
from classes.asset import Asset


# def main():
gang1 = Gang('da dorfs')
strength_list = []

# %%
for i in range(0,10):
    print(f'Day {i}')
    gang1.activate()
    strength_list.append(gang1.get_strength())

print(strength_list)

strength = pd.DataFrame(strength_list, columns=['Strength'])

# %%
fig = px.line(strength, y="Strength")
fig.show()
# %%
