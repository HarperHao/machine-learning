import numpy as np


def LCS_LENGTH(X, Y):
    m = len(X)  # length of X
    n = len(Y)  # length of Y
    b = np.array([[None] * (n + 1)] * (m + 1))
    c = np.array([[0] * (n + 1)] * (m + 1))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i, j] = 'diag'
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i, j] = 'up'
            else:
                c[i, j] = c[i, j - 1]
                b[i, j] = 'left'
    return b, c


def print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return None
    if b[i, j] == 'diag':
        print_LCS(b, X, i - 1, j - 1)
        print(X[i - 1], end=' ')
    elif b[i, j] == 'up':
        print_LCS(b, X, i - 1, j)
    else:
        print_LCS(b, X, i, j - 1)


X = 'conservatives'
Y = 'breather'

b, c = LCS_LENGTH(X, Y)
print_LCS(b, X, len(X), len(Y))
