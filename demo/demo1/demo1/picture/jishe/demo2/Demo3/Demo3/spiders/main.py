# from scrapy.cmdline import execute
#
# execute("scrapy crawl zuowumianji".split())
import numpy as np


# LU分解
def LU_Decompose(matrix):
    rows, columns = np.shape(matrix)
    if rows != columns:
        print("所输入的矩阵必须是方阵！")
        return
    L = np.eye(rows)
    U = np.triu(matrix)  # 先求出U矩阵(化上三角矩阵）
    # 求L矩阵（主对角线为1的下三角矩阵）
    L[:, 0] = matrix[:, 0] / U[0][0]  # L的第一列
    for k in range(1, columns - 1):  # 从第2列到columns-1列
        for i in range(k + 1, rows):  # 从第3行到第rows行
            sum = 0
            for j in range(0, k - 1):  # (0,0)不行
                x = L[i][j] * U[j][k]
                sum = sum + x
            L[i][k] = (matrix[i][k] - sum) / U[k][k]
    return L, U


# 解LY=b
def solve_equation1(L, b):
    columns = np.shape(b)[0]
    y = []
    y.append(b[0][0])  # y0=b0
    for i in range(1, columns):  # 求yi
        sum = 0
        for j in range(i):
            sum = sum + L[i][j] * y[j]
        y_ = b[i][0] - sum
        y.append(y_)
    return y


# 解UX=Y
def solve_equation2(U, Y):
    columns = np.shape(Y)[0]
    X = [i for i in range(columns)]  # 先给X初始化
    if U[columns - 1] == 0:
        X[columns - 1] = Y[columns - 1] / U[columns - 1][columns - 1]  # Xcolumns-1=Ycolumns-1/U[columns-1][columns-1]
    else:
        X[columns - 1] = 0


matrix = np.array([[2, -1, 1],
                   [4, 1, -1],
                   [1, 1, 1]])
rows, columns = np.shape(matrix)
L, U = LU_Decompose(matrix)
# b = np.eye(rows)
b = np.array([1, 5, 0]).reshape(3, 1)
# y = solve_equation1(L, b)
print(L, U)
