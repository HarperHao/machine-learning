"""
结合Matplotlib与numpy绘制函数f(x)=sin2(x-2)e-x2
"""
import matplotlib.pyplot as plt
import numpy as np


def fun():
    x = np.linspace(-100, 100, 256)
    y = np.sin(x - 2) * np.sin(x - 2) * np.e ** (-x ** 2)
    plt.plot(x, y)
    plt.show()


fun()
