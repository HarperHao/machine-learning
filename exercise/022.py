"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
求出这个数列的前20项之和。
用三种方法实现
"""


def fun1():
    mu = 1
    zi = 2
    sum = zi / mu
    a = mu
    b = zi
    for i in range(19):
        mu = b
        zi = a + b
        a = mu
        b = zi
        sum = sum + zi / mu
    print(sum)


def fun2():
    fenzi = 2
    fenmu = 1
    sum = 0
    for i in range(20):
        sum = fenzi / fenmu + sum
        fenzi, fenmu = (fenzi + fenmu), fenzi
    print(sum)


def fun3():
    l=[]
    fenzi = 2
    fenmu = 1
    for i in range(20):
         l.append(fenzi/fenmu)
         fenzi, fenmu = (fenzi + fenmu), fenzi
    
    print(sum(l))


fun1()
fun2()
fun3()
