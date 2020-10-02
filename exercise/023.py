"""
题目：求1+2!+3!+...+20!的和
用两种方法实现
"""


# 求前n项阶乘之和
def fun1(n):
    if n == 1:
        return 1
    else:
        sum = 1
        for i in range(1, n + 1):
            sum = sum * i
        return fun1(n - 1) + sum


def fun2(n):
    sum = 1
    for i in range(2, n + 1):  # [2,n]的阶乘
        temp = 1
        for j in range(1, i + 1):
            temp = temp * j
        sum = sum + temp
    return sum


print(fun1(20))
print(fun2(20))
