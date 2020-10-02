"""
请编写一个函数fun ()，它的功能是：验证尼科彻斯定理。
即：任何一个整数的立方都可以写成一串连续奇数的和。
fun()的输入参数为待验证的数，返回值为连续奇数的个数，通过数组返回这些连续奇数。
"""
import numpy as np


def fun(n):
    list1 = []
    x = n ** 2 - n + 1
    list1.append(x)
    for i in range(1, n):
        x=x+2
        list1.append(x)
    arr = np.array(list1)
    return arr, n


n = eval(input("请输入一个整数："))
arr, sum = fun(n)
print("连续奇数个数为：", sum)
print(arr)
