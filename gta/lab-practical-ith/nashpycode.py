import numpy as np
import nashpy as nash

# Senator payoff matrix
A = np.array([
    [10, 10, 0, 0],
    [5, 15, 5, 15]
])

# Challenger payoff matrix
B = np.array([
    [5, 5, 10, 10],
    [15, 0, 15, 0]
])

game = nash.Game(A, B)

equilibria = game.support_enumeration()

print("Nash Equilibria:\n")
for eq in equilibria:
    print(eq)