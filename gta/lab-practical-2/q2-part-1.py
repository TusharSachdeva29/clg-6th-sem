import nashpy as nash
import numpy as np

# Payoff matrices
A = np.array([[2, 0],
              [0, 1]])   # Husband payoff

B = np.array([[1, 0],
              [0, 2]])   # Wife payoff

# Create game
game = nash.Game(A, B)

# Compute Nash equilibria
print("Nash Equilibria are:")
for eq in game.support_enumeration():
    print(eq)
