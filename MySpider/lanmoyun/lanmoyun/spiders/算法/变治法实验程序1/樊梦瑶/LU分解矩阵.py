import numpy as np
import sys

def LU(A):
    n = A.shape[0]
    E = np.mat(np.eye(n))
    L = np.mat(np.eye(n))
    U = A.copy()
    for i in range(n):
        L[i + 1:, i] = U[i + 1:, i] / U[i, i]
        E[i + 1:, :] = E[i + 1:, :] - L[i + 1:, i] * E[i, :]
        U[i + 1:, :] = U[i + 1:, :] - L[i + 1:, i] * U[i, :]
    E1 = np.mat(np.eye(n))
    for i in range(n - 1, -1, -1):
        E[i, :] = E[i, :] / U[i, i]
        E1[i, :] = E1[i, :] / U[i, i]
        U[i, :] = U[i, :] / U[i, i]
        E[:i, :] = E[:i, :] - U[:i, i] * E[i, :]
        E1[:i, :] = E1[:i, :] - U[:i, i] * E1[i, :]
        U[:i, :] = U[:i, :] - U[:i, i] * U[i, :]
    E2 = np.mat(np.eye(n))
    for i in range(n):
        E2[i + 1:, :] = E2[i + 1:, :] - L[i + 1:, i] * E2[i, :]
        L[i + 1:, :] = L[i + 1:, :] - L[i + 1:, i] * U[i, :]
    return L,U,E1,E2

if __name__ == "__main__":
    A = np.mat([[1,1,0], [1,0,1], [0,1,1]])
    A_dim = A.shape[0]
    L,U,E1,E2=LU(A)
    print("L矩阵为:")
    print(L)
    print("L的逆为:")
    print(E2)
    print("U矩阵为:")
    print(U)
    print("U的逆为:")
    print(E1)
    print("A的逆为:")
    print(E1*E2)