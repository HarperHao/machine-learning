"""
将列表中值小于n的元素放到n前面，大于n的元素放到n的后面
"""
import random


def demo(x, n):
    t1 = [i for i in x if i < n]
    t2 = [i for i in x if i > n]
    return t1 + [n] + t2


x = list(range(1, 10))
random.shuffle(x)
print(demo(x, 4))
