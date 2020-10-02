"""
请编写一个函数fun()，它的功能是：求解一个数各个数据位的平方和，
一个数各数字的平方求和最终得到1或145，返这个数。主函数已经实现结果的输出
"""


def fun(number):
    sum = 0
    for i in number:
        sum = sum + int(i) ** 2
    if sum == 1 and sum == 145:
        return number
    else:
        return sum


number = input("请输入一个数：")
x = fun(number)
print(x)
