def fun(n):
    a = [[0] * n for i in range(n)]
    i = 0
    j = n // 2
    a[i][j] = 1
    for k in range(2, n ** 2 + 1):
        i = i - 1
        j = j + 1
        # if i >= 0 and j <= n - 1:
        #     a[i][j] = k
        # i-1=1,j+1=3
        if i < 0 and j <= n - 1:
            i = n - 1
        elif i >= 0 and j > n - 1:
            j = 0

        elif (i == -1 and j == n) or a[i][j] != 0:  # 右上角或重复,必须先判断在右上角在判断是否重复
            i = i + 2
            j = j - 1

        a[i][j] = k

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()


n = int(input("请输入n阶幻方(n为奇数)："))
fun(n)
