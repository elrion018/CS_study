import sys
import heapq


def init(st):
    dist = dict()
    q = []
    for i in range(1, N+1):
        if i != st:
            dist[i] = inf
        else:
            dist[i] = 0
    heapq.heappush(q, (dist[st], st))

    return dist, q


def Di(graph, start, end):
    dist, q = init(st)
    while q:
        a = heapq.heappop(q)[1]
        for i in range(1, N+1):
            if graph[a][i] != inf:

                cal_dist = dist[a] + graph[a][i]

                if cal_dist < dist[i]:
                    dist[i] = cal_dist
                    heapq.heappush(q, (dist[i], i))

    return dist[end]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
inf = sys.maxsize

graph = [[inf] * (N+1) for _ in range(N+1)]


for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    if graph[x][y] > cost:
        graph[x][y] = cost
st, end = map(int, sys.stdin.readline().split())

print(Di(graph, st, end))
