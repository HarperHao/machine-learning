"""
有1、2、3、4个数字，
能组成多少个互不相同且无重复数字的三位数？都是多少？
"""


def fun():
    count = 0
    list1 = [1, 2, 3, 4]
    for i in list1:
        for j in list1:
            for k in list1:
                print(str(i) + str(j) + str(k))
                count = count + 1
    print("共能组成{}个不重复的数".format(count))


fun()
