"""
利用math库中的阶乘函数计算组合数
"""

import math


def Cni(n, i):
    return int(math.factorial(n) / math.factorial(i) / math.factorial(n - i))


print(Cni(6, 2))
