import numpy as np
import matplotlib.pyplot as plt


def Draw_Bernulia():
    bins_num = 20
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.subplot(1, 3, 1)
    a = np.random.binomial(100, 0.6, 1000)
    plt.title("Bernoulli:试验次数=100次,每次成功概率=0.6", fontsize=15)
    plt.xlabel('成功次数',fontsize=15)
    plt.ylabel('概率',fontsize=15)
    plt.hist(a, bins_num, density=1, color='blue')
    # 第二个图
    plt.subplot(1, 3, 2)
    b = np.random.binomial(1000, 0.6, 1000)
    plt.title("Bernoulli:试验次数=1000次,每次成功概率=0.6", fontsize=15)
    plt.xlabel('成功次数',fontsize=15)
    plt.ylabel('概率',fontsize=15)
    plt.hist(b, bins_num, density=1, color='red')
    # 第三个图
    plt.subplot(1, 3, 3)
    c = np.random.binomial(1100, 0.6, 1000)
    plt.title("Bernoulli:试验次数=1100次,每次成功概率=0.6", fontsize=15)
    plt.xlabel('成功次数',fontsize=15)
    plt.ylabel('概率',fontsize=15)
    plt.hist(c, bins_num, density=1, color='green')
    plt.show()


Draw_Bernulia()
