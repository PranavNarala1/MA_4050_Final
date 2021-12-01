import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#from equationGenerator import getLambda

#states = np.arange(0, 101, 1)
#print(states)
#getLambda(state_parameter)

def display_heatmap(time):
    state_lambas = gen_lambas('matrix.csv')
    state_lambas = np.array(state_lambas)
    state_lambas = np.resize(state_lambas, (10, 10))
    for x in range(1, 3, 5, 7, 9):
        state_lambas[x] = state_lambas[x][::-1]

    states_at_time = np.array(state_lambas)

    for row in state_lambas:
        for col in row:
            state_lambas[row][col] = state_lambas[row][col][time]

    heat_map = sns.heatmap(states_at_time)

    plt.clf()
    plt.title('Probabilities of States on the Board')

    plt.imshow(heat_map)
    plt.show()

display_heatmap(10)
