#imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import equationGenerator
import seaborn as sns

#defining getHeatMap
def getHeatMap(turn):
    states_dataframe = equationGenerator.genLambdas()
    row_value = turn / 0.01
    state_values = states_dataframe.to_numpy()[int(row_value)]
    state_values = np.resize(state_values, (10, 10))

    for x in [1, 3, 5, 7, 9]:
        state_values[x] = state_values[x][::-1]

    state_values = np.flip(state_values, 0)
    heat_map = sns.heatmap(state_values)

getHeatMap(1)
getHeatMap(5)
getHeatMap(10)
getHeatMap(15)
getHeatMap(20)
getHeatMap(25)
getHeatMap(30)
getHeatMap(35)
getHeatMap(40)
getHeatMap(45)
getHeatMap(50)
getHeatMap(55)
getHeatMap(60)
getHeatMap(65)
getHeatMap(70)
getHeatMap(75)
getHeatMap(80)
getHeatMap(85)
getHeatMap(90)
getHeatMap(95)
getHeatMap(100)