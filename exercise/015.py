"""
用函数实现如下要求：
（1）随机生成20个学生的成绩
（2）判断这20个学生成绩的等级
"""
import random

list1 = {}
for i in range(20):
    a = random.randint(0, 100)
    if a<=100 and a>=90:
        grade='A'
    elif a<90 and a>=80:
        grade='B'
    elif a<80 and a>=60:
        grade='C'
    elif a<60:
        grade='D'
    print("分数：{}   等级：{}".format(a,grade))

