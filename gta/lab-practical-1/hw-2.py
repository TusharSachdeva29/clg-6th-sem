import numpy as np

# Strategy encoding
# 0 = Deny
# 1 = Confess

# Payoff matrices
P1 = np.array([
    [-1, -10],   # P1 denies
    [ 0,  -5]    # P1 confesses
])

P2 = np.array([
    [-1,   0],   # P2 denies
    [-10, -5]    # P2 confesses
])

print("Best Responses:\n")

bestP1 = np.zeros((2, 2), dtype=bool)
bestP2 = np.zeros((2, 2), dtype=bool)

# Best responses of Player 1
for p2 in range(2):
    mx = np.max(P1[:, p2])
    for p1 in range(2):
        if P1[p1][p2] == mx:
            bestP1[p1][p2] = True
    br = np.argmax(P1[:, p2])
    print(f"P1 best response to P2 = {'Deny' if p2 == 0 else 'Confess'} "
          f"is {'Deny' if br == 0 else 'Confess'}")

print()

# Best responses of Player 2
for p1 in range(2):
    mx = np.max(P2[p1, :])
    for p2 in range(2):
        if P2[p1][p2] == mx:
            bestP2[p1][p2] = True
    br = np.argmax(P2[p1, :])
    print(f"P2 best response to P1 = {'Deny' if p1 == 0 else 'Confess'} "
          f"is {'Deny' if br == 0 else 'Confess'}")

print("\nNash Equilibria:")
found = False

for p1 in range(2):
    for p2 in range(2):
        if bestP1[p1][p2] and bestP2[p1][p2]:
            found = True
            print(f"({ 'Deny' if p1 == 0 else 'Confess' }, "
                  f"{ 'Deny' if p2 == 0 else 'Confess' })")

if not found:
    print("No pure Nash Equilibrium exists")
