import numpy as np

A = np.array([
    [10, 10, 0, 0],
    [5, 15, 5, 15]
])

B = np.array([
    [5, 5, 10, 10],
    [15, 0, 15, 0]
])

rows = 2
cols = 4

print("Pure Strategy Nash Equilibria:\n")

for i in range(rows):
    for j in range(cols):

        senator_best = True
        challenger_best = True

        # check senator deviation
        for ii in range(rows):
            if A[ii][j] > A[i][j]:
                senator_best = False

        # check challenger deviation
        for jj in range(cols):
            if B[i][jj] > B[i][j]:
                challenger_best = False

        if senator_best and challenger_best:
            print("NE at strategy:", i, j)