"""
请编写一个函数fun ()，实现验证输入参数n是否为完数。
如果一个数恰好等于它的因子之和，这个数就称为“完全数”。
例如：6的因子是1、2、3，而6=1+2+3，因此6是“完全数”。
函数fun()输入参数整数n表示待验证数，
返回值为1表示n是完数，返回值为0表示n不是完数。
主函数实现输出，并求出10000以内的所有完全数。。
"""


def fun(n):
    list1 = []
    for i in range(1, n):
        if n % i == 0:
            list1.append(i)
    if n == sum(list1):
        return 1
    else:
        return 0


# 返回一万以内的所有完数
def fun1(count):
    for n in range(2, count):
        list1 = []
        for i in range(1, n):
            if n % i == 0:
                list1.append(i)
        if n == sum(list1):
            print(n)

fun1(10000)
n = eval(input("请输入要判断的数："))
result = fun(n)
print(result)
