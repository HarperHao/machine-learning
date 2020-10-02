import random
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons


def creat_dots(count):
    dots = [[0] * 2 for i in range(count)]
    x = []
    y = []
    for i in range(count):
        dots[i][0] = random.randrange(1000)
        dots[i][1] = random.randrange(1000)
    # 按x轴排好序
    dots.sort()
    for i in range(count):
        x.append(dots[i][0])
        y.append(dots[i][1])
    return dots, x, y


def distance(x, y):
    return float(math.sqrt(x * x + y * y))


# 传进来数组左右元素的下标
def coloset(left, right):
    # mindis最短距离，a、b存储最近对点的坐标
    global mindis, a, b, ax, dots
    length = right - left
    # 只有一个点，或者没有点
    if length <= 0:
        dis = 999999999
        return dis
    # 有两个点
    elif length == 1:
        # 此时直接求距离即可
        dis = distance(dots[right][0] - dots[left][0], dots[right][1] - dots[left][1])
        # 用蓝色的线画出
        ax.plot([dots[left][0], dots[right][0]], [dots[left][1], dots[right][1]], color='b')
        plt.pause(0.5)
        ax.lines.pop()
        # 更新最近点对
        if dis < distance(a[0] - b[0], a[1] - b[1]):
            a = [dots[right][0], dots[right][1]]
            b = [dots[left][0], dots[left][1]]

        return dis
    # 有三个及三个以上的点
    else:
        # 获得中间点的下标
        mid = int((right + left) / 2)
        # 获得中间的线的横坐标
        midline = dots[mid][0]
        # 中位线用黄色来表示
        ax.plot([midline, midline], [0, 1000], color='yellow')
        plt.pause(0.5)
        # 求左边集合的最短距离
        dis1 = coloset(left, mid)
        # 求右边集合的最短距离
        dis2 = coloset(mid + 1, right)
    # 比较得出左右两边最短的距离
    if dis1 <= dis2:
        md = dis1
    else:
        md = dis2
    # 更新最短距离
    if md < mindis:
        mindis = md
    # 子集合并
    # 构建两条竖线
    points = []
    for dot in dots[left:right + 1]:
        if abs(dot[0] - midline) <= md:
            points.append(dot)
    # 按y轴进行排序
    # points.sort(key=lambda x: x[1])
    for i in range(len(points)):
        # 如果是右边的点直接pass
        if (points[i][0] - midline > 0):
            continue
        # 此时i代表的是左边的点,所以要找到右边的点
        for j in range(len(points)):
            if (points[j][0] - midline < 0) or (i == j):
                continue
            else:
                ax.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], color='black')
                plt.pause(0.3)
                # 消除线
                ax.lines.pop()
                plt.pause(0.2)
                temp_dis = distance(points[i][0] - points[j][0], points[i][1] - points[j][1])
                if temp_dis < mindis:
                    mindis = temp_dis
                    a = [points[i][0], points[i][1]]
                    b = [points[j][0], points[j][1]]
    ax.lines.pop()
    return mindis


def change_midline(label):
    global ax, a, b
    plt.cla()
    # color = {'yellow': ax.plot([a[0], b[0]], [a[1], b[1]], c='y'),
    #          'green': ax.plot([a[0], b[0]], [a[1], b[1]], c='g'),
    #          'brown': ax.plot([a[0], b[0]], [a[1], b[1]], c='brown')}
    # j = color[label]
    ax.scatter(a[0], a[1], color='r', marker=label)
    ax.scatter(b[0], b[1], color='r', marker=label)
    plt.draw()


def creat_matplotlib():
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']

    global mindis, a, b, ax, dots, fg, x, y
    # 初始化最短距离
    mindis = 1000 * 1000
    # 初始化最近对点
    a = [1000, 1000]
    b = [0, 0]
    fg = plt.figure()
    ax = fg.add_subplot(111)
    #plt.subplots_adjust(left=0.3)
    ax.grid()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    plt.subplots_adjust(left=0.3)
    # 开启交互模式
    plt.ion()
    count = int(input('输入生成点的数量：'))
    dots, x, y = creat_dots(count)
    # 设置按钮
    axesbgcolor = 'cornflowerblue'
    ax1 = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axesbgcolor)
    radio1 = RadioButtons(ax1, ('x', 'p', '*'))
    # 先将所有点绘制在图上
    ax.plot(x, y, color='b', marker='.')
    for xx, yy in zip(x, y):
        plt.text(xx, yy + 0.5, (xx, yy), ha='center', va='bottom', fontsize=7.5)
    print("距离：", coloset(0, count - 1))
    print("最近对：", a, b)
    ax.set_title('最近对坐标为：{},{} 距离为:{:.2f}'.format(a, b, coloset(0, count - 1)))
    ax.scatter(a[0], a[1], color='r', marker='^')
    ax.scatter(b[0], b[1], color='r', marker='^')
    ax.plot([a[0], b[0]], [a[1], b[1]], c='r')
    plt.ioff()
    radio1.on_clicked(change_midline)
    plt.show()


if __name__ == "__main__":
    creat_matplotlib()
