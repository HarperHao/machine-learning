# from tkinter import *
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def maxvalue(self, n, c, w, v):
#         """
#          测试数据：
#          n = 6  物品的数量，
#          c = 10 书包能承受的重量，
#          w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
#          v = [2, 3, 1, 5, 4, 3] 每个物品的价值
#          """
#         # 价值表初始化
#         value = [[0 for i in range(c + 1)] for k in range(n + 1)]
#         for i in range(1, n + 1):
#             for k in range(1, c + 1):
#                 # 表格一行一行的填写
#                 value[i][k] = value[i - 1][k]
#                 # 判断是否可以替换，替换时，需要用到上一行的价值
#                 if k >= w[i - 1] and (value[i][k] < value[i - 1][k - w[i - 1]] + v[i - 1]):
#                     value[i][k] = value[i - 1][k - w[i - 1]] + v[i - 1]
#         return value
#
#     def createWidget(self):
#         self.number = Label(root, text="物品的数量:")
#         self.number.place(x=15, y=20, width=70, height=30)
#         self.Number = StringVar()
#         self.number_text = Entry(root, width=10, textvariable=self.Number)
#         self.number_text.place(x=85, y=20, width=100, height=25)
#         self.Max_Weight = Label(root, text="背包承受的最大重量:")
#         self.Max_Weight.place(x=200, y=20, width=120, height=30)
#         self.MW = IntVar()
#         self.Max_Weight_text = Entry(root, text=self.MW)
#         self.Max_Weight_text.place(x=320, y=20, width=120, height=30)
#         self.Value_List = Label(root, text="物品价值列表:")
#         self.Value_List.place(x=0, y=80, width=110, height=30)
#         self.VL = StringVar()
#         self.Value_List_text = Entry(root, text=self.VL)
#         self.Value_List_text.place(x=100, y=80, width=110, height=30)
#         self.Widget_List = Label(root, text="物品重量列表:")
#         self.Widget_List.place(x=200, y=80, width=110, height=30)
#         self.WL = StringVar()
#         self.Widget_List_text = Entry(root, text=self.WL)
#         self.Widget_List_text.place(x=300, y=80, width=110, height=30)
#         self.button = Button(root, text='计算', command=self.getValue)
#         self.button.place(x=631, y=19, width=30, height=30)
#         self.Text = Text(root, width=50, height=12, bg='gray')
#         self.Text.place(relx=0.18, rely=0.18)
#
#     def getValue(self):
#         self.value22 = self.maxvalue(int(self.number_text.get()), (int(self.Max_Weight_text.get())),
#                                      [int(_) for _ in list(self.Widget_List_text.get().split())],
#                                      [int(_) for _ in list(self.Value_List_text.get().split())])
#         count = 1.0
#         print(type((self.number_text.get())))
#         # self.Text.insert(INSERT,"test")
#         while count <= (float(self.number_text.get()) + 1):
#             for j in range(1, self.MW.get() + 1):
#                 self.Text.insert(END, str(self.value22[int(count) - 1][j]))
#                 self.Text.insert(INSERT, '  ')
#             self.Text.insert(INSERT, '\n')
#             count = count + 1
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.geometry("800x700+400+48")
#     root.title("背包问题")
#     app = Application(master=root)
#
#     root.mainloop()
# def func(a):
#     return lambda b:a+b
# print(func(3))
# import numpy as np
# print(np.ones((3,4,5)))

"""TCP服务端"""
# import socket
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('192.168.1.103', 8888))
# client_socket.send('No.2 hello!'.encode())
# recv_data = client_socket.recv(1024)
# print('接受到的数据为'.format(recv_data))
# client_socket.close()
# a = [1, [2, 4, 5]]
# a[1][2] = str(a[1][2])
# print(a)
# from wordcloud import WordCloud
# import PIL.Image as image
# import numpy as np
# import jieba
#
# def trans_CN(text):
#    word_list = jieba.cut(text)
#    result = " ".join(word_list)
#    return result
#
#
# with open("E:\学习\python\wordcloud.txt") as fp:
#    text = fp.read()
#    text = trans_CN(text)
#    mask = np.array(image.open("F:\wordcloud\image\love.jpg"))
#    wordcloud = WordCloud(mask=mask,font_path="C:\Windows\Fonts\STXINGKA.TTF").generate(text)
#    image_produce = wordcloud.to_image()
#    image_produce.show()
# def fab(n):
#     if n == 1 or n == 2:
#         return 1
#     return fab(n-1) + fab(n-2)
#
# print(fab(5))
# import turtle as t
# # for i in range(4):
# #     t.seth(90*(i+1))
# #     t.circle(200,90)
# #     t.seth(-90+i*90)
# #     t.circle(200,90)
# import random
# print(random.randint(240, 560))
# import random
# import math
# import matplotlib.pyplot as p
#
# input = int(input('输入生成点的数量：'))
# dot = [[0] * 3 for i in range(input)]
# mindis = 1000 * 1000
# fg = p.figure()
# cn = fg.add_subplot(1, 1, 1)
# cn.set_xlim(0, 1000)
# cn.set_ylim(0, 1000)
# p.ion()
# a = [1000, 1000]
# b = [0, 0]
# x = []
# y = []
# for i in range(input):
#     dot[i][0] = random.randrange(1000)
#     dot[i][1] = random.randrange(1000)
#     dot[i][2] = 0
# dot.sort()
# for i in range(input):
#     x.append(dot[i][0])
#     y.append(dot[i][1])
#
#
# def distance(x, y):
#     return float(math.sqrt(x * x + y * y))
#
#
# def dac(left, right):
#     global mindis, a, b
#     len = right - left
#     length = (right + left)
#     cn.scatter(x, y, color='b', marker='.')
#     if len <= 0:
#         dis = 9999999999999
#         return dis
#     elif len == 1:
#         dis = distance(dot[right][0] - dot[left][0], dot[right][1] - dot[left][1])
#         cn.plot([dot[left][0], dot[right][0]], [dot[left][1], dot[right][1]], color='r')
#         p.pause(0.1)
#         cn.lines.pop()
#         p.pause(0.1)
#         if dis < distance(a[0] - b[0], a[1] - b[1]):
#             a = [dot[right][0], dot[right][1]]
#             b = [dot[left][0], dot[left][1]]
#         return dis
#     else:
#         n = int(length / 2)
#         midline = (dot[n][0] + dot[n + 1][0]) / 2
#         cn.plot([midline, midline], [0, 1000], color='b')
#         p.pause(0.1)
#         dis1 = dac(left, n)
#         dis2 = dac(n + 1, right)
#     if dis1 <= dis2:
#         md = dis1
#     else:
#         md = dis2
#     if mindis > md:
#         mindis = md
#     for i in dot[left:n + 1]:
#         if abs(i[0] - midline) <= md:
#             for j in dot[n + 1:right + 1]:
#                 if j[0] - midline <= md:
#                     if i[1] - md <= j[1] <= i[1] + md:
#                         dis3 = distance(i[0] - j[0], i[1] - j[1])
#                         if mindis > dis3:
#                             mindis = dis3
#                         cn.plot([i[0], j[0]], [i[1], j[1]], color='r')
#                         p.pause(0.1)
#                         cn.lines.pop()
#                         p.pause(0.1)
#                         if dis3 < distance(a[0] - b[0], a[1] - b[1]):
#                             a = [i[0], i[1]]
#                             b = [j[0], j[1]]
#     cn.lines.pop()
#     return mindis
#
#
# list = []
# c = [1000, 1000]
# d = [0, 0]
# for i in range(input):
#     for j in range(i + 1, input):
#         list.append(distance(dot[i][0] - dot[j][0], dot[i][1] - dot[j][1]))
#         if distance(dot[i][0] - dot[j][0], dot[i][1] - dot[j][1]) < distance(c[0] - d[0], c[1] - d[1]):
#             c = [dot[i][0], dot[i][1]]
#             d = [dot[j][0], dot[j][1]]
# list.sort()
# print("检验：", list[0], c, d)
# print("距离：", dac(0, input - 1))
# print("最近对：", a, b)
# cn.plot([a[0], b[0]], [a[1], b[1]], c='b')
# p.pause(10)

import random
import numpy
import math
import matplotlib.pyplot as plt


def caculateDis(x1, y1, x2, y2):
   return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def mergePoints(points, l, mid, r):
   pl = points[l:mid:]
   i = l
   j = 0
   k = mid
   while i < r:
       if j < len(pl) and (k == r or pl[j][1] <= points[k][1]):
           points[i] = pl[j]
           i += 1
           j += 1
       if k < r and (j == len(pl) or pl[j][1] > points[k][1]):
           points[i] = points[k]
           i += 1
           k += 1
   return points


def getClosest(points, l, r):
   resultx = resulty = []
   if r - l == 2:
       return caculateDis(points[l][0], points[l][1], points[r - 1][0], points[r - 1][1]), [points[l][0],
                                                                                            points[r - 1][0]], [
                  points[l][1], points[r - 1][1]]
   if r - l == 3:
       pp = points[l:r]
       pp.sort(key=lambda x: x[1])
       points[l:r] = pp
       dis1 = caculateDis(points[l][0], points[l][1], points[r - 1][0], points[r - 1][1])
       dis2 = caculateDis(points[l + 1][0], points[l + 1][1], points[r - 1][0], points[r - 1][1])
       dis3 = caculateDis(points[l][0], points[l][1], points[l + 1][0], points[l + 1][1])
       mindis = min(dis1, dis2, dis3)
       if mindis == dis1:
           ansx = [points[l][0], points[r - 1][0]]
           ansy = [points[l][1], points[r - 1][1]]
       elif mindis == dis2:
           ansx = [points[l + 1][0], points[r - 1][0]]
           ansy = [points[l + 1][1], points[r - 1][1]]
       else:
           ansx = [points[l][0], points[l + 1][0]]
           ansy = [points[l][1], points[l + 1][1]]
       return mindis, ansx, ansy
   mid = (l + r) // 2
   d1, px1, py1 = getClosest(points, l, mid)
   d2, px2, py2 = getClosest(points, mid, r)
   if d1 < d2:
       d = d1
       resultx = px1
       resulty = py1
   else:
       d = d2
       resultx = px2
       resulty = py2
   points = mergePoints(points, l, mid, r)
   choice = []
   for i in range(l, r):
       if (abs(points[i][0] - points[mid][0]) < d):
           choice.append(points[i])
   for i in range(0, len(choice)):
       for j in range(i + 1, len(choice)):
           if choice[j][1] - choice[i][1] >= d:
               break
           else:
               dist = caculateDis(choice[i][0], choice[i][1], choice[j][0], choice[j][1])
               if dist < d:
                   d = dist
                   resultx = [choice[i][0], choice[j][0]]
                   resulty = [choice[i][1], choice[j][1]]
   return d, resultx, resulty


def main():
   points = []
   maxsize = 10
   lower = -100
   upper = 100
   x = [random.randint(-100, 100) for i in range(maxsize)]
   y = [random.randint(-100, 100) for i in range(maxsize)]
   plt.scatter(x, y, s=10)
   for i in range(maxsize):
       points.append([x[i], y[i]])
   for xx, yy in zip(x, y):
       plt.text(xx, yy + 0.8, (xx, yy), ha='center', va='bottom', fontsize=7.5)
   points.sort(key=lambda x: x[0])
   ans, ansx, ansy = getClosest(points, 0, maxsize)
   print("最短距离为：", ans)
   print("最近的两个点为 (%d,%d) , (%d,%d)" % (ansx[0], ansy[0], ansx[1], ansy[1]))
   plt.scatter(ansx[0], ansy[0], color='r')
   plt.scatter(ansx[1], ansy[1], color='r')
   plt.plot(ansx, ansy, color='r')
   plt.show()

if __name__=='__main__':
   main()
