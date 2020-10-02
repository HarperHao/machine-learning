"""
使用random产生自己想要的随机序列
输入自己想要的数据，从自己输入的数据里面产生随机数
2020.2.21
"""
import random

# random.seed(3)
str1 = input("请输入您想要的随机数并用空格分隔开：")
lst = str1.split(" ")
you_want = list(map(int, lst))
length = len(you_want)
for i in range(length):
    result = random.choice(you_want)
    you_want.remove(result)
    print("产生的第{}个随机数为{}".format(i+1, result))
