import string


# num是string，len和m是Int
def fun(num, length, m):
    # 位权法
    if m != 16:  # 二进制或者八进制
        sum = 0
        for i in range(length):  # 每一位的位权
            num_ = int(num[i])
            sum = sum + num_ * m ** (length - i - 1)
    else:  # 十六进制
        X = string.hexdigits[10:]
        sum = 0
        for i in range(length):
            if num[i] in X:
                a = X.index(num[i]) % 6
                sum = sum + (a + 10) * m ** (length - i - 1)
            else:
                sum = sum + int(num[i]) * m ** (length - i - 1)
    return sum


m = int(input("请输入（2/8/16）确定输入几进制数："))
num = input("请输入这个数：")
length = int(len(num))
sum = fun(num, length, m)
print("{}的十进制数为{}".format(num, sum))
