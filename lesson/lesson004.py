
import matplotlib.pyplot as plt
import random
import math


def sort_angle(dots, p):
    dots1 = dots[::]
    distance_list = []
    cos_list = []
    point_list = []
    del dots1[0]  # 在这个列表里面没有源点
    length = len(dots1)
    for i in range(length):
        point_ = dots1[i]
        point = (point_[0] - p[0], point_[1] - p[1])
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        distance_list.append(distance)
        cos = point[0] / distance
        if cos not in cos_list:
            cos_list.append(cos)
            point_list.append(point_)
        # 角度(向量与x轴的夹角)相同的话就要判断哪个距离原点的距离更远
        else:
            index = cos_list.index(cos)  # 原来那个相同角度在列表中的下标索引
            distance_one = distance_list[index]
            if distance_one >= distance:  # 如果旧的距离大于新的距离
                distance_list.pop()  # 将刚添加进去的distance弹出
            else:  # 新的距离大于旧的距离
                del distance_list[index]  # 删除旧的距离
                del cos_list[index]  # 删除旧的角度
                del point_list[index]  # 删除旧的点
                cos_list.append(cos)  # 添加新的角度
                point_list.append(point_)  # 添加新的点
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
    # print(points_list)
    # print(sorted_points)
    return sorted_points


def creat():
    count = eval(input("请输入生成点的数量："))
    x_ = []
    y_ = []
    for i in range(count):
        x = random.uniform(-10, 10)  # 产生-10到10的浮点数
        y = random.uniform(-10, 10)
        x_.append(x)
        y_.append(y)
    dots = list(zip(x_, y_))
    dots.sort(key=lambda x: (x[1], x[0]))
    return dots


def multi_cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


# 逆时针扫描
def graham(dots):
    p = dots[0]
    sorted_points = sort_angle(dots, p)
    stack = []
    m = len(sorted_points)
    stack.append(p)
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])
    for i in range(2, m):
        length = len(stack)
        top_point = stack[length - 1]
        last_point = stack[length - 2]
        next_point = sorted_points[i]
        v1 = [top_point[0] - last_point[0], top_point[1] - last_point[1]]
        v2 = [next_point[0] - last_point[0], next_point[1] - last_point[1]]
        cross_multi = multi_cross(v1, v2)
        while cross_multi <= 0:  # 顺时针
            stack.pop()
            length = len(stack)
            top_point = stack[length - 1]
            last_point = stack[length - 2]
            next_point = sorted_points[i]
            v1 = [top_point[0] - last_point[0], top_point[1] - last_point[1]]
            v2 = [next_point[0] - last_point[0], next_point[1] - last_point[1]]
            cross_multi = multi_cross(v1, v2)
        stack.append(next_point)
    return stack


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


if __name__ == "__main__":
    dots = creat()
    result = graham(dots)
    draw(result, dots)
