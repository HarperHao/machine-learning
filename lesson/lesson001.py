"""
a/b得到的数是float
而range()中必须为int
a={2,2,3}
b={2,2}
a&b={2}
这是因为集合是无序不重复的
"""


# 求两个数的最大公约数（正整数）
def commonFactor(num1, num2):
    result = 1
    m = num1
    n = num2
    if (num1 == 1):
        print("{}与{}的最大公约数是{}".format(num1, num2, num1))
    elif (num2 == 1):
        print("{}与{}的最大公约数是{}".format(num1, num2, num2))
    elif (num1 == num2):
        print("{}与{}的最大公约数是{}".format(num1, num2, num2))
    elif (num1 > num2):  # 求出较小值的公因数序列来
        temp2 = decompose(num2)
        for i in temp2:
            if num1 % i == 0:
                result *= i
                num1 /= i
        print("{}与{}的最大公约数是{}".format(m, n, result))
    elif (num2 > num1):
        temp2 = decompose(num1)
        for i in temp2:
            if num2 % i == 0:
                result *= i
                num2 /= i
        print("{}与{}的最大公约数是{}".format(m, n, result))


# 求一个数分解的质因数
def decompose(num):
    temp = []
    while num != 1:
        for i in range(2, num + 1):  # 如果num是负数的话这里就有问题了
            if num % i == 0:
                temp.append(i)
                num = num // i
                break  # 要重新求num的质因数
    return (temp)


print("功能1：求某个数字的所有质因数")
print("功能2：求两个数字的最大公约数")
flag = eval(input("请输入要执行的功能的编号："))
if flag == 1:
    num = eval(input("请输入一个数字："))
    temp = decompose(num)
    print("{}的所有质因数有：".format(num), end='')
    for j in temp:
        print(j, end=',')
elif flag == 2:
    a = eval(input("请输入第一个数字："))
    b = eval(input("请输入第二个数字："))
    commonFactor(a, b)
