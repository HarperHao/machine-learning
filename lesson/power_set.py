"""
求幂集
"""
import random
import string


def all_subset(set1):
    length = len(set1)
    lists = [[] for i in range(2 ** length)]
    for i in range(2 ** length):
        # 将一个十进制数转换为二进制数,并将这个二进制数高位补0，然后将它的每一位拆分
        x = bin(i).replace('0b', '')
        y = list(map(str, x.zfill(length)))
        for j in range(length):
            if y[j] == '1':
                lists[i].append(set1[j])
    return lists


def creat_set():
    number = eval(input("请输入集合中元素的个数："))
    strings = string.ascii_letters + string.digits + string.punctuation
    set1 = random.sample(strings, number)  # 选取的元素不重复
    return set1


set1 = creat_set()
lists = all_subset(set1)
lists.sort(key=lambda x: len(x))
print("原集合为：", set1)
print("幂集为：", lists)
