def fun(Adjacent, src, n):
    Inf = float('inf')
    distance = [Inf] * n
    distance[src] = 0
    book = [0] * n

    u = src
    for i in range(n - 1):
        book[u] = 1
        next_u, minVal = None, float('inf')
        for v in range(n):
            w = Adjacent[u][v]
            if w == Inf:
                continue
            if not book[v] and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                if distance[v] < minVal:
                    next_u, minVal = v, distance[v]
        u = next_u
    print(distance)


Inf = float('inf')

Adjacentacent = [[0, 1, 12, Inf, Inf, Inf],
                 [Inf, 0, 9, 3, Inf, Inf],
                 [Inf, Inf, 0, Inf, 5, Inf],
                 [Inf, Inf, 4, 0, 13, 15],
                 [Inf, Inf, Inf, Inf, 0, 4],
                 [Inf, Inf, Inf, Inf, Inf, 0]]
Src, N = 0, 6

fun(Adjacentacent, Src, N)
