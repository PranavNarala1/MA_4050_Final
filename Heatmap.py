import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import equationGenerator
import seaborn as sns

def getHeatMap(turn):
    states_dataframe = equationGenerator.genLambdas()
    row_value = turn / 0.01
    state_values = states_dataframe.to_numpy()[int(row_value)]
    state_values = np.resize(state_values, (10, 10))

    for x in [1, 3, 5, 7, 9]:
        state_values[x] = state_values[x][::-1]

    heat_map = sns.heatmap(state_values)

getHeatMap(10)
