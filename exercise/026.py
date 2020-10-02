"""
题目：某个公司采用公用电话传递数据，
数据是四位的整数，在传递过程中是加密的，
加密规则如下：
每位数字都加上5,
然后用和除以10的余数代替该数字，
再将第一位和第四位交换，第二位和第三位交换。
"""
import string
import random


def fun():
    list1 = string.digits
    password = random.choices(list1, k=4)
    temp = []
    temp1 = []
    # a, b, c, d = password
    for i in password:
        i = 5 + int(i)
        temp.append(i)
    for j in temp:
        j = j % 10
        temp1.append(j)
    temp1[0], temp1[3] = temp1[3], temp1[0]
    temp1[1], temp1[2] = temp1[2], temp1[1]
    temp1 = map(str, temp1)
    print("原密码为：", ''.join(password))
    print("加密后的密码为：",''.join(temp1))


fun()
