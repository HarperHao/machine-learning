"""
螺旋矩阵（m*n）方阵
"""


def fun(m, n):
    a = [[0] * n for i in range(m)]
    row_start = 0
    row_end = m - 1
    column_start = 0
    column_end = n - 1
    k = 1
    while row_start <= row_end and column_start <= column_end:
        # 第一层循环
        for j in range(column_start, column_end + 1):  # 上
            a[row_start][j] = k
            k = k + 1
        for i in range(row_start + 1, row_end):  # 右

            a[i][column_end] = k
            k = k + 1
        for j in range(column_end, column_start - 1, -1):  # 下
            a[row_end][j] = k
            k = k + 1
        for i in range(row_end - 1, row_start, -1):  # 左
            a[i][column_start] = k
            k = k + 1
        column_start = column_start + 1
        column_end = column_end - 1
        row_start = row_start + 1
        row_end = row_end - 1
    if m % 2 == 1:
        a[m // 2][n // 2] = k - 1

    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print()


m = int(input("请输入矩阵的行："))
n = int(input("请输入矩阵的列："))
fun(m, n)
