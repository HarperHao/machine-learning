import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def Draw_Ber():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # 第一个图的绘制
    k1 = np.arange(0, 100)  # x值
    n1 = 100
    p = 0.6
    Ber1 = stats.binom.pmf(k1, n1, p)  # y值
    # xnew = np.linspace(k1.min(), k1.max(), 800)
    # ynew = spline(k1, Ber, xnew)
    plt.subplot(1, 3, 1)
    plt.title("Bernoulli:试验次数={},成功概率={}".format(n1, p), fontsize=15)
    plt.xlabel(u"成功的次数", )
    plt.ylabel(u"概率")
    plt.plot(k1, Ber1, 'bo-')
    #第二个图的绘制
    plt.subplot(1,3,2)
    k2=np.arange(1000)
    n2=1000
    Ber2=stats.binom.pmf(k2,n2,p)
    plt.title("Bernoulli:实验次数={},成功概率={}".format(n2, p), fontsize=15)
    plt.xlabel(u"成功的次数", )
    plt.ylabel(u"概率")
    plt.plot(k2,Ber2,'bo-')

    #第三个图的绘制
    plt.subplot(1, 3, 3)
    k3 = np.arange(1000+100)
    n3 = 1100
    Ber3 = stats.binom.pmf(k3, n3, p)
    plt.title("Bernoulli:实验次数={},成功概率={}".format(n3, p), fontsize=15)
    plt.xlabel(u"成功的次数", )
    plt.ylabel(u"概率")
    plt.plot(k3, Ber3, 'bo-')

    plt.show()


Draw_Ber()
