import nashpy as nash
import numpy as np

A = np.array([
    [3, 0],
    [5, 1]
])

B = np.array([
    [3, 5],
    [0, 1]
])

game = nash.Game(A, B)

equilibria = list(game.support_enumeration())

for eq in equilibria:
    print(eq)
