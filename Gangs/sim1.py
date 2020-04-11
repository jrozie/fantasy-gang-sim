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

# %%
strength = []
for i in range(0,10):
    strength.append(gang1.get_strength())
    gang1.recruit(1)

print(strength)

strength = pd.DataFrame(strength, columns=['Strength'])

# %%
fig = px.line(strength, y="Strength")
fig.show()
# %%
