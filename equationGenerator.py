import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate all functions to solve the system
def genLambdas(filename="coeffmat.csv"):
    # Read coefficient matrix in
    mat = np.genfromtxt(filename, delimiter=" ")

    # Time variables
    t = 0
    t_max = 100
    dt = 0.01
    t_list = [t]

    # Function variables
    state = np.zeros((len(mat), 1))
    state[0] = 1
    state_list = np.array([state.reshape(len(mat))])

    # Loop over conditions
    while t < t_max:
        # RK4, modeled after https://www.youtube.com/watch?v=0LzDiScAcJI
        v1 = np.matmul(mat, state)
        v2 = np.matmul(mat, state + dt/2 * v1)
        v3 = np.matmul(mat, state + dt/2 * v2)
        v4 = np.matmul(mat, state + dt * v3)

        # Update x and y
        state += dt * (v1 + 2*v2 + 2*v3 + v4) / 6

        # Update time
        t += dt

        # Store the state
        state_list = np.append(state_list, [state.reshape(len(mat))], axis=0)

        # Store time
        t_list.append(t)

    # Convert the state_list into a dataframe
    return pd.DataFrame(state_list)

if __name__ == "__main__":
    table = genLambdas()
    print(table.head(3))
    print(table.tail(3))