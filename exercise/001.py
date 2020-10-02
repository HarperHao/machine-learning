"""
请编写一个函数fun()，它的功能是：将n（2、8、16）进制数转换为十进制数。
输入包含一个n进制数，返回这个数的十进制数值，主函数已经实现整数的输入和十进制数的输出。
"""


def fun(choice, number):
    if choice == 1:
        print("二进制数{0} -----> 十进制数为{1}".format(number, int(number, 2)))
    elif choice == 2:
        print("八进制数{0} -----> 十进制数为{1}".format(number, int(number, 8)))
    elif choice == 3:
        print("十六进制数{0} -----> 十进制数为{1}".format(number, int(number, 16)))


def judge(number):
    a = number[:2]

    if a == '0b' or a == '0B':  # 二进制
        # return 1
        choice = 1
    elif a == '0o' or a == '0O':  # 八进制
        # return 2
        choice = 2
    elif a == '0x' or a == '0X':  # 十六进制
        # return 3
        choice = 3
    else:
        # return None
        choice = None
    return choice


print("1.二进制：0b/0B开头")
print("2.八进制：0o/0O开头")
print("3.十六进制：0x/0X开头")
# choice = eval(input("请输入要选择的功能："))
number = input("请输入一个数：")
choice = judge(number)
if choice == None:
    print("输入格式错误")
else:
    fun(choice, number)
