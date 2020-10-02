"""
请编写程序，生成随机密码。具体要求如下：
使用random库，采用0x1010作为随机数种子。
密码由26个字母大小写、10个数字字符和!@#$%^&*等8个特殊符号组成。
每个密码长度固定为10个字符。
程序运行每次产生10个密码，每个密码一行。
每次产生10个密码首字符不能一样。
程序运行后产生的密码保存在“随机密码.txt”文件中。
"""
import random
import string


def fun():
    strings = string.digits + string.ascii_letters + "!@#$%^&*"
    length = 10
    for i in range(10):  # 产生十个密码
        a = []
        while len(a) < length:  # 给密码固定长度
            _ = random.choice(strings)
            if i == 0:  # 第一个密码不需要判断首字母
                a.append(_)
            else:  # 之后的密码
                if _ == x:
                    continue
                a.append(_)
        x = a[0]

        with open("随机密码.txt", 'a') as f:
            a_ = ''.join(a)
            f.write(a_ + '\n')  # write只能写字符


fun()
