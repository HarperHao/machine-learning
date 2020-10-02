"""
题目：打印出杨辉三角形
"""


def fun(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    numRows = numRows - 2
    rList = [[1], [1, 1]]
    while numRows > 0:
        newList = [1]
        for i in range(len(rList[-1]) - 1):
            newList.append(rList[-1][i] + rList[-1][i + 1])
        newList.append(1)
        rList.append(newList)
        numRows = numRows - 1
    for i in range(len(rList)):
        print(rList[i])


numberRows = int(input("请输入行数："))
fun(numberRows)
