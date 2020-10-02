def cycle(num, k):
    flag = 0
    if (num == 1):
        return flag
    else:
        flag = (cycle(num - 1, k) + k) % num

        return flag


i = input('请输入总人数和要报的数（用逗号分隔开）:')
num, k = map(int, i.split(','))
people = [i for i in range(41)]
flag = cycle(num, k)
print('最后幸存者的编号为{}号'.format(flag + 1))
