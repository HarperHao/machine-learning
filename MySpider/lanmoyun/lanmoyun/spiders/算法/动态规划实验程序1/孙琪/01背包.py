import turtle as t

def paint(x, y, res, W):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.down()
    t.write('背包容量为: ' + str(W) + ', 可取得的最大价值为: ' + str(res), font=('consolas', 15, 'normal'))

def draw(x, y, r, p=0, w=0, v=0, should=0):
    if v and w:
        t.color('red')
    if should:
        t.penup()
        t.setx(x)
        t.sety(y)
        t.pendown()
        t.circle(r)
    t.color('black')
    t.penup()
    t.setx(x)
    t.sety(y + r - 10)
    t.pendown()
    if p:
        t.write(p, font=('consolas', 15, 'normal'))
    if v and w:
        t.penup()
        t.setx(x - 60)
        t.sety(y - 30)
        t.pendown()
        t.write("体积: " + str(w) + ", 价值: " + str(v), font=('consolas', 13, 'normal'))


N = eval(input('请输入物品的个数: '))

W = eval(input('请输入背包的大小: '))

v = [0 for i in range(N)]
w = [0 for i in range(N)]
dp = [0 for i in range(W + 1)]
bag = [[] for i in range(W + 1)]
for i in range(N):
    w[i], v[i] = map(int, input('请输入第' + str(i + 1) + '个物品的体积和价值: ').split())

for i in range(N):
    for j in range(W, w[i] - 1, -1):
        if dp[j] < dp[j - w[i]] + v[i]:
            dp[j] = dp[j - w[i]] + v[i]
            bag[j] = bag[j - w[i]] + [i]

r = 40
x = [-650]
y = [250]
for i in range(N):
    x.append(x[i - 6] if i >= 6 else x[i] + 200)
    y.append(y[i - 6] - 200 if i >= 6 else y[i])
    draw(x[i], y[i], r, i + 1, 0, 0, 1)
print('最终选择的物品序列为: ' + str(bag[W]))
for i in range(N):
    draw(x[i], y[i], r + 20, 0, w[i], v[i], i in bag[W])

paint(200, -200, dp[W], W)
print('可取得的最大价值为: ' + str(dp[W]))
t.done()