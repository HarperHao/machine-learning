import turtle as t

N = eval(input('请输入数组的大小: '))
dp = [1 for i in range(N)]
a = list(map(int, input('请输入n个正整数: ').split()))
G = [[a[i]] for i in range(N)]
for i in range(N):
    for j in range(i):
        if a[j] < a[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            G[i] = G[j] + [a[i]]
sx = -600
sy = 200
t.penup()
t.setx(sx)
t.sety(sy)
t.pendown()
t.write('原序列: ', font={'consolas', 15, 'normal'})
sx += 100
for i in range(N):
    t.penup()
    t.setx(sx)
    t.sety(sy)
    t.pendown()
    t.write(a[i], font={'consolas', 15, 'normal'})
    sx += 30

most = 0
res = []
for i in range(N):
    if dp[i] > most:
        most = dp[i]
        res = G[i]

sx = -600
sy = 30
t.penup()
t.setx(sx)
t.sety(sy)
t.pendown()
t.write('最长上升子序列: ', font={'consolas', 15, 'normal'})
sx += 180
print('最大上升子序列的长度为: ' + str(most))
print('最大上升子序列为: ' + str(res))
for i in range(N):
    t.penup()
    t.setx(sx)
    t.pendown()
    if a[i] in res:
        t.color('red')
        res.remove(a[i])
    else:
        t.color('black')
    t.write(a[i], font={'consolas', 15, 'normal'})
    sx += 30
t.done()