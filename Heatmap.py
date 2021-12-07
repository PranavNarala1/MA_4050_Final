import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from equationGenerator import genLambdas

#states = np.arange(0, 101, 1)
#print(states)
#getLambda(state_parameter)

def display_heatmap(turn):
    state_lambdas = genLambdas()
    state_lambdas = np.array(state_lambdas)
    state_lambdas = np.resize(state_lambdas, (10, 10))
    for x in [1, 3, 5, 7, 9]:
        state_lambdas[x] = state_lambdas[x][::-1]

    states_at_turn = np.zeros(state_lambdas.shape)
    print(states_at_turn)

    for row in range(len(state_lambdas)):
        for col in range(len(state_lambdas[row])):
            states_at_turn[row][col] = state_lambdas[row][col](turn)

    print(state_lambdas[6][7](10))
    print(states_at_turn)
    heat_map = sns.heatmap(states_at_turn)

    plt.clf()
    plt.title('Probabilities of States on the Board')

    plt.imshow(heat_map)
    plt.show()

display_heatmap(10)
