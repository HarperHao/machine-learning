"""
求1+2+3+...+100，用三种方法实现
"""


def fun1():
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    print(sum)


def fun2():
    print((1 + 100) * 100 // 2)


def fun3():
    print(sum(range(1, 101)))


fun1()
fun2()
fun3()
