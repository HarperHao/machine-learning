import random
import math
import matplotlib.pyplot as plt


def creat():
    count = eval(input("请输入生成点的数量："))
    x_ = []
    y_ = []
    for i in range(count):
        x = random.randint(-10, 10)  # 产生-10到10的浮点数
        y = random.randint(-10, 10)
        x_.append(x)
        y_.append(y)
    dots = list(zip(x_, y_))
    dots.sort(key=lambda x: (x[0], x[1]))
    return dots, count


def dealTop(first, last, dots, temp):
    max = 0
    index = -1
    firstPoint = dots[first]
    lastPoint = dots[last]
    firstPoint_x = firstPoint[0]
    firstPoint_y = firstPoint[1]
    lastPoint_x = lastPoint[0]
    lastPoint_y = lastPoint[1]
    for i in range(first + 1, last):
        nowPoint = dots[i]
        nowPoint_x = nowPoint[0]
        nowPoint_y = nowPoint[1]
        area = firstPoint_x * lastPoint_y + nowPoint_x * firstPoint_y + lastPoint_x * nowPoint_y - nowPoint_x * lastPoint_y - lastPoint_x * firstPoint_y - firstPoint_x * nowPoint_y
        if area > max:
            index = i
            max = area

    if index != -1:  # 说明找到了max点
        temp[index] = 1
        dealTop(first, index, dots, temp)
        dealTop(index, last, dots, temp)


def dealBottom(first, last, dots, temp):
    max = 0
    index = -1
    firstPoint = dots[first]
    lastPoint = dots[last]
    firstPoint_x = firstPoint[0]
    firstPoint_y = firstPoint[1]
    lastPoint_x = lastPoint[0]
    lastPoint_y = lastPoint[1]
    for i in range(first + 1, last):
        nowPoint = dots[i]
        nowPoint_x = nowPoint[0]
        nowPoint_y = nowPoint[1]
        area = firstPoint_x * lastPoint_y + nowPoint_x * firstPoint_y + lastPoint_x * nowPoint_y - nowPoint_x * lastPoint_y - lastPoint_x * firstPoint_y - firstPoint_x * nowPoint_y
        if area < max:
            index = i
            max = area

    if index != -1:  # 说没找到了max点
        temp[index] = 1
        dealBottom(first, index, dots, temp)
        dealBottom(index, last, dots, temp)
    #


def draw(result, dots):
    draw_result = result[::]
    for dot in dots:
        plt.scatter(dot[0], dot[1], marker='o', c='y')
    # 连线
    result_ = result[0]
    draw_result.append(result_)
    # draw_result.insert(0,result_)
    for i in range(len(result)):
        first_dot = draw_result[i]
        second_dot = draw_result[i + 1]
        line = list(zip(first_dot, second_dot))
        plt.plot(line[0], line[1], color='r')
    plt.show()


# 按逆时针方向排序
def sort_angle(dots, p):
    dots1 = dots[::]
    cos_list = []
    point_list = []
    length = len(dots1)
    for i in range(length):
        point_ = dots1[i]
        point = (point_[0] - p[0], point_[1] - p[1])
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        if distance==0:
            cos_list.append(1)
            point_list.append(p)
        else:
            cos = point[0] / distance
            cos_list.append(cos)
            point_list.append(point_)
    # cos_list.sort()  # 从小到大排序
    acos_list = []
    for i in range(len(cos_list)):
        temp = math.acos(cos_list[i])
        acos_list.append(temp)
    points_list = list(zip(point_list, acos_list))
    points_list.sort(key=lambda x: x[1])
    sorted_points = []
    for i in range(len(points_list)):
        temp = points_list[i][0]
        sorted_points.append(temp)
    return sorted_points


def dividied(dots, count):
    result = []
    for i in range(count):
        temp[i] = 0
    temp[0] = 1
    temp[count - 1] = 1
    dealTop(0, count - 1, dots, temp)
    dealBottom(0, count - 1, dots, temp)
    for i in range(count):
        if temp[i] == 1:
            result.append(dots[i])
    result.sort(key=lambda x: (x[1], x[0]))
    p = result[0]
    result_ = sort_angle(result, result[0])
    draw(result_, dots)


if __name__ == "__main__":
    temp = {}
    dots, count = creat()
    #dots = [(-7, 3), (-7, 5), (-5, 10), (-2, -2), (-2, 5)]
    #count = 5
    dividied(dots, count)
