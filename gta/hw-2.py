import numpy as np

# Strategy encoding
# 0 = Deny
# 1 = Confess

# payoff[player][p1_strategy][p2_strategy]

P1 = np.array([
    [-1, -10],   # P1 denies
    [ 0,  -5]    # P1 confesses
])

P2 = np.array([
    [-1,   0],   # P2 denies
    [-10, -5]    # P2 confesses
])

print("Best Responses:\n")

# Best response of Player 1
for p2 in range(2):
    br = np.argmax(P1[:, p2])
    print(f"P1 best response to P2 = {'Deny' if p2 == 0 else 'Confess'} "
          f"is {'Deny' if br == 0 else 'Confess'}")

print()

# Best response of Player 2
for p1 in range(2):
    br = np.argmax(P2[p1, :])
    print(f"P2 best response to P1 = {'Deny' if p1 == 0 else 'Confess'} "
          f"is {'Deny' if br == 0 else 'Confess'}")

print("\nNash Equilibrium: (Confess, Confess)")
