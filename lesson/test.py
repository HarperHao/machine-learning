"""
编写函数
接受一个字符串
返回一个元组
元组第一个是大写字母个数，第二个是小写字母的个数
"""


def count(a):
    b = [0, 0]
    for i in a:
        if i.isupper():
            b[0] = b[0] + 1
        elif i.islower():
            b[1] = b[1] + 1
    b = tuple(b)
    return b


a = input("请输入字符串：")
b=count(a)
print("源字符串为：", a)
print("统计结果为：", b)


def __x(self):
    return self.__value


def __y(self, v):
    self.__value = v


value = property(__x, __y)


def show(self):
    print(self.__value)