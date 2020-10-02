EDGE_MAX=1000#边的最大长度为1000
dis=[EDGE_MAX for _ in range(7)]
pan=[i for i in range(7)]
begin=eval(input("请输入从0到6的哪个节点开始:"))
edge=[[EDGE_MAX for i in range(7)] for j in range(7)]
def init(edge,n,EDGE_MAX):
    edge[0][1]=12
    edge[0][5]=16
    edge[0][6]=14
    edge[1][2]=10
    edge[1][5]=7
    edge[2][3]=3
    edge[2][4]=5
    edge[2][5]=6
    edge[3][4]=4
    edge[4][5]=2
    edge[4][6]=8
    edge[5][6]=9
    for i in range(n):
        for j in range(i,n):
            if edge[i][j]!=EDGE_MAX:
                edge[j][i]=edge[i][j]
def dijkstra(begin,n,map,dis,pan):
    station_vertex=[0 for i in range(n)]
    pan[begin]=begin
    dis[begin]=0
    station_vertex[begin]=1
    pre=begin
    while True:
        for j in range(n):
            if station_vertex[j]==0 and dis[j]>dis[pre]+map[pre][j]:
                dis[j]=dis[pre]+map[pre][j]
                pan[j]=pre
        for i in range(n):
            if station_vertex[i]==0:
                pre=i
                break
        for i in range(pre,n):
            if station_vertex[i]==0 and dis[i]<dis[pre]:
                pre=i
        if station_vertex[pre]==1:
            break
        station_vertex[pre]=1
init(edge,7,EDGE_MAX)
dijkstra(begin,7,edge,dis,pan)
for i in range(7):
    print('点{}到点{}的最短路径长度为{}'.format(begin,i,dis[i]))