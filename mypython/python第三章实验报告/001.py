"""
itertools的groupby()函数
"""
import itertools


def group(v):
    if v > 10:
        return '大于10'
    elif v < 5:
        return '小于5'
    else:
        return '大于5小于10'


x = range(20)
y = itertools.groupby(x, group)
for k, v in y:
    print(k, ':', list(v))
