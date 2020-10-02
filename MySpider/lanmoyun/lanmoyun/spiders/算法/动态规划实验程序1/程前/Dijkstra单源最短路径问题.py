MAX=9999999999999
n=int(input("有几个节点:"))

print("输入图的邻接矩阵:")

ls=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        ls[i][j]=int(input())
for i in range(n):
    ls[i][i]=MAX

d=[MAX]*n     #储存0到其他节点的最短路径


for i in range(n-1):       #n个节点要找n-1个路径
    p=ls[0].index(min(ls[0]))
    m=ls[0][p]
    d[p]=m
    for j in range(1,n):
        if (d[j]+ls[j][p])<m:
            d[p]=d[j]+ls[j][p]
            m=d[p]

    ls[0][p]=MAX

for i in range(1,n):
    print("0->%d的最短距离:%d"%(i,d[i]))

    #课上5阶临接矩阵如下：
    0
    10
    999
    30
    100
    999
    0
    50
    999
    999
    999
    999
    0
    999
    10
    999
    999
    20
    0
    60
    999
    999
    999
    999
    0