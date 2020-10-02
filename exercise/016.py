"""
创建一个10*10的数组，
并且边框是1，
里面是0，如下图所示：
"""


def fun():
    a = [[0] * 10 for i in range(10)]
    row1 = 0
    row2 = 10
    column1 = 0
    column2 = 10
    for j in range(column2):
        a[row1][j] = 1
        a[row2 - 1][j] = 1
    for i in range(row1 + 1, row2 - 1):
        a[i][column1] = 1
        a[i][column2 - 1]=1

    for i in range(10):
        for j in range(10):
            print(a[i][j], end=' ')
        print()


fun()
