"""
题目：将一个正整数分解质因数。
例如：输入90,打印出90=2*3*3*5。
"""


def fun(number):
    list1 = fun1(number)
    list2 = []
    for i in list1:
        while number != 1:
            if number % i == 0:
                number = number / i
                list2.append(i)
            else:
                break
    return list2


# 求出[2,number]间所有的质因数
def fun1(number):
    list1 = []
    list1.append(2)
    j = 2
    for i in range(3, number + 1):
        while j < i:
            if i % j != 0:
                j = j + 1
            else:
                break
        if j == i:
            list1.append(i)
    return list1


number = int(input("请输入一个数："))
list2 = fun(number)

print('{} = '.format(number), end='')
for i in range(len(list2)):
    if i == len(list2) - 1:
        print('{}'.format(list2[i]))
    else:
        print('{}'.format(list2[i]), end=' * ')
