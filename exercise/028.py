"""
交换两个变量的值，用两种方法实现
"""


def fun1(a, b):
    a, b = b, a
    return a, b


def fun2(a, b):
    c = a
    a = b
    b = c
    return a, b


a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
print(fun1(a, b))
print(fun2(a, b))
