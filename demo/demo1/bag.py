def bag(n, c, w, v):
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j < w[i - 1]:
                value[i][j] = value[i - 1][j]
            else:
                value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])
    # 背包总容量够放当前物体，取最大价值
    return value


def show(n, c, w, value, name):
    print('最大价值为:', value[n][c])
    x = [0 for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = 1
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print(name[i], end=',')


if __name__ == '__main__':
    n = 5  # 六个物品
    c = 10  # 背包容量
    w = [2, 2, 6, 5, 4]  # 物品重量
    v = [6, 3, 5, 4, 6]  # 物品价值
    name = ['a', 'b', 'c', 'd', 'e']
    value = bag(n, c, w, v)
    show(n, c, w, value, name)
