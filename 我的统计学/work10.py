"""蒙特卡洛法计算无理数PI"""
import numpy as np
import matplotlib.pyplot as plt


# 绘制第一象限内的图形
def draw(count):
    in_ = 0
    out_ = 0
    plt.xlim(xmax=1, xmin=0)
    plt.ylim(ymax=1, ymin=0)
    for i in range(count):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if (x ** 2 + y ** 2 < 1):
            in_ = in_ + 1
            plt.scatter(x, y, s=2, c="red")
        else:
            out_ = out_ + 1
            plt.scatter(x, y, s=2, c="blue")
        print('\r{:.2f}%'.format(i / count*100), end='')
    plt.title("n={} PI={}".format(count, in_ / (in_ + out_) * 4))
    plt.show()


# count = int(input("请输入生成点的数量:"))
draw(30000)
