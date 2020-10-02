"""
输出乘法口诀表
"""
for i in range(1, 10):
    for j in range(i, 10):
        print("{}*{}={}".format(i, j, i * j), end=" ")
    print()
