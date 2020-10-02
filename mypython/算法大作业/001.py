import random
import math
import matplotlib.pyplot as plt


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


def dac(left, right):  # 传进来数组左右元素的下标
    # mindis最短距离，a、b存储最近对点的坐标
    global mindis, a, b
    len = right - left
    # 只有一个点，或者没有点
    if len <= 0:
        dis = 9999999999999
        return dis
    # 有两个点
    elif len == 1:
        # 此时直接求距离即可
        dis = distance(dots[right][0] - dots[left][0], dots[right][1] - dots[left][1])
        # 用蓝色的线画出
        cn.plot([dots[left][0], dots[right][0]], [dots[left][1], dots[right][1]], color='b')
        plt.pause(0.5)
        cn.lines.pop()
        # plt.pause(0.5)
        # 更新最近点对
        if dis < distance(a[0] - b[0], a[1] - b[1]):
            a = [dots[right][0], dots[right][1]]
            b = [dots[left][0], dots[left][1]]
        return dis
    # 有三个及三个以上的点
    else:
        # 获得中间点的坐标
        mid = int((right + left) / 2)
        # 获得中间的线的横坐标
        midline = dots[mid][0]
        # midline = (dots[n][0] + dots[n + 1][0]) / 2
        # 中位线用黄色来表示
        cn.plot([midline, midline], [0, 1000], color='yellow')
        plt.pause(0.5)
        # 求左边集合的最短距离
        dis1 = dac(left, mid)
        # 求右边集合的最短距离
        dis2 = dac(mid + 1, right)
    # 比较得出左右两边最短的距离
    if dis1 <= dis2:
        md = dis1
    else:
        md = dis2
    # 更新最短距离
    if mindis > md:
        mindis = md
    # 子集合并
    # i是集合左边的点
    for i in dots[left:mid + 1]:
        # 找出SL在P1区域的点
        if abs(i[0] - midline) <= md:
            # j是集合右边的点
            for j in dots[mid + 1:right + 1]:
                # 找出SR在区域P2的点
                if j[0] - midline <= md:
                    # 进行扫描（这一步之前不用对y轴进行排序吗？）
                    # i和j这两个点的纵坐标相差在一个md之内
                    if i[1] - md <= j[1] <= i[1] + md:
                        # 求出i和j两点的距离
                        dis3 = distance(i[0] - j[0], i[1] - j[1])
                        # 如果合并时的线的距离更短则更新最短距离
                        if mindis > dis3:
                            mindis = dis3
                            a = [i[0], i[1]]
                            b = [j[0], j[1]]
                        # 用绿色的线表示合并线的连接
                        cn.plot([i[0], j[0]], [i[1], j[1]], color='black')
                        plt.pause(0.5)
                        # 消除线
                        cn.lines.pop()
                        plt.pause(0.5)
                        #
                        # #if dis3 < distance(a[0] - b[0], a[1] - b[1]):
                        #     a = [i[0], i[1]]
                        #     b = [j[0], j[1]]
    cn.lines.pop()
    return mindis


if __name__ == "__main__":

    # 初始化最短距离
    mindis = 1000 * 1000
    # 初始化最近对点
    a = [1000, 1000]
    b = [0, 0]
    fg = plt.figure()
    cn = fg.add_subplot(111)
    cn.set_xlim(0, 1000)
    cn.set_ylim(0, 1000)
    # 开启交互模式
    plt.ion()
    count = int(input('输入生成点的数量：'))
    dots, x, y = creat_dots(count)
    #检验
    list = []
    c = [1000, 1000]
    d = [0, 0]
    for i in range(count):
        for j in range(i + 1, count):
            list.append(distance(dots[i][0] - dots[j][0], dots[i][1] - dots[j][1]))
            if distance(dots[i][0] - dots[j][0], dots[i][1] - dots[j][1]) < distance(c[0] - d[0], c[1] - d[1]):
                c = [dots[i][0], dots[i][1]]
                d = [dots[j][0], dots[j][1]]
    list.sort()
    print("检验：", list[0], c, d)

    # 先将所有点绘制在图上
    cn.scatter(x, y, color='b', marker='.')
    print("距离：", dac(0, count - 1))
    print("最近对：", a, b)
    cn.scatter(a[0],a[1],color='r',marker='^')
    cn.scatter(b[0], b[1], color='r', marker='^')
    cn.plot([a[0], b[0]], [a[1], b[1]], c='r')
    plt.ioff()
    plt.show()
