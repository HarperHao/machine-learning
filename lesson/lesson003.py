def all_subset(goods, value, weigh):
    length = len(goods)
    lists = [[] for i in range(2 ** length)]
    weighs = [[] for i in range(2 ** length)]
    values = [[] for i in range(2 ** length)]
    for i in range(2 ** length):
        # 将一个十进制数转换为二进制数,并将这个二进制数高位补0，然后将它的每一位拆分
        x = bin(i).replace('0b', '')
        y = list(map(str, x.zfill(length)))
        z = list(reversed(y))
        for j in range(length):
            if z[j] == '1':
                lists[i].append(goods[j])
                values[i].append(value[j])
                weighs[i].append(weigh[j])
    return lists, values, weighs


# 编号：（价值，重量）
goods = ['a', 'b', 'c', 'd', 'e']#编号
value = [6, 3, 5, 4, 6]#价值
weigh = [2, 2, 6, 5, 4]#重量
max_weighs = 10#背包最大承重
# dict1 = dict(zip(goods, zip(value, weigh)))

sum_weighs = []
sum_values = []
new_sum_values = []
index = []  # 标号

lists, values, weighs = all_subset(goods, value, weigh)
for i in weighs:
    sum_weighs.append(sum(i))
for i in values:
    sum_values.append(sum(i))
sum_weighs = list(enumerate(sum_weighs))
sum_values = list(enumerate(sum_values))
lists = list(enumerate(lists))
for i in sum_weighs:
    if i[1] <= max_weighs:
        index.append(i[0])  # int类型
for i in index:
    new_sum_values.append(sum_values[i])

value_sort = sorted(new_sum_values, key=lambda x: x[1], reverse=True)
result = value_sort[0][0]
print('在背包容量为{}的条件下，应选择包含{}的情况最好，此时背包重量为{}，背包种物品总价值为{}'
      .format(max_weighs, lists[result][1], sum_weighs[result][1], sum_values[result][1]))
