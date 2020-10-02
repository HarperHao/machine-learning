"""
从A到E的最短路径
"""


def creat():
    filename = 'graph.txt'
    graph = {}
    data = []
    with open(filename, 'r')as f:
        for line in f:
            info = line.split(',')
            #print(info)
            data.append(info)
        for m in data[::-1]:
            key = m[0]
            graph[key] = []
            if key != 'E':
                for i in m[1:]:
                    node, cost = i.split()
                    node.strip()
                    cost.strip()
                    cost = int(cost)
                    graph[key].append((node, cost))
    return graph


def update_distance(graph, distance):
    newDistance = {}
    for key in graph:
        if key == 'E':
            distance[key] = 0
        else:
            nodes = graph[key]
            distance[key] = min(node[1] + distance[node[0]] for node in nodes)

    return distance


def printPath(graph, distance):
    list1 = []
    list1.append('A')
    start = 'A'
    while start != 'E':
        for node in graph[start]:
            if distance[start] == (distance[node[0]] + node[1]):
                list1.append(node[0])
                start = node[0]
    return list1


distance = {}
graph = creat()
#print(graph)
MAX_NUM = 999
# 距离初始化
for key in graph:
    distance[key] = MAX_NUM
distance['E'] = 0
#print(update_distance(graph, distance))
distance = update_distance(graph, distance)
list1 = printPath(graph, distance)
for item in list1:
    print(item, end='->')
print("\n最短路径长为：", distance["A"])
