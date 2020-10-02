"""
请编写一个函数fun ()，它的功能是：验证四方定理。
四方定理是数论中的重要定理，
它可以叙述为：所有的自然数至多只要用4个数的平方和就可以表示出来。
例如：
25=1×1+2×2+2×2+4×4
99=1×1+1×1+4×4+9×9
fun()的输入参数为待验证的数，输出为一共有多少组解，通过数组a组成验证的表达式。
"""

from math import sqrt


def fun(n):
    count = 0
    for i in range(1, int(sqrt(n)) + 1):
        for j in range(i + 1):
            for k in range(j + 1):
                for m in range(k + 1):
                    if i ** 2 + j ** 2 + k ** 2 + m ** 2 == n:
                        print("{}={}*{}+{}*{}+{}*{}+{}*{}".format(n, i, i, j, j, k, k, m, m))
                        count = count + 1
    print("总数为：", count)


n = eval(input("请输入要验证的数："))
fun(n)
