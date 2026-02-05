import numpy as np

# Payoff matrices
# Husband payoff
A = np.array([[2, 0],
              [0, 1]])

# Wife payoff
B = np.array([[1, 0],
              [0, 2]])

strategies = ["Opera", "Football"]

print("Payoff Matrix (Husband, Wife):")
for i in range(2):
    for j in range(2):
        print(f"{strategies[i]} , {strategies[j]} -> ({A[i][j]}, {B[i][j]})")

print("\n==============================")
print("1. PURE NASH EQUILIBRIA")
print("==============================")

pure_NE = []

# Check all outcomes
for i in range(2):
    for j in range(2):

        # Husband best response
        husband_best = A[i][j] >= A[1-i][j]

        # Wife best response
        wife_best = B[i][j] >= B[i][1-j]

        if husband_best and wife_best:
            pure_NE.append((strategies[i], strategies[j]))

print("Pure Nash Equilibria are:")
for eq in pure_NE:
    print(eq)

print("\n==============================")
print("2. MIXED NASH EQUILIBRIUM")
print("==============================")

# Solve mixed equilibrium manually
# Let Husband plays Opera with probability p
# Let Wife plays Opera with probability q

# Wife indifferent condition:
# p*1 + (1-p)*0 = p*0 + (1-p)*2
# p = 2(1-p)
p = 2/3

# Husband indifferent condition:
# q*2 + (1-q)*0 = q*0 + (1-q)*1
# 2q = 1-q
q = 1/3

print("Mixed Nash Equilibrium:")
print(f"Husband plays Opera with probability {p:.3f}")
print(f"Husband plays Football with probability {1-p:.3f}")

print(f"Wife plays Opera with probability {q:.3f}")
print(f"Wife plays Football with probability {1-q:.3f}")
