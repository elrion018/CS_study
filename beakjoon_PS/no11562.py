import sys


def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    graph[i][j] = 0
                elif i != k and j != k:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


n, m = map(int, sys.stdin.readline().split())

inf = sys.maxsize

graph = [[inf for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u, v, b = map(int, sys.stdin.readline().split())
    if b == 1:
        graph[u][v] = 0
        graph[v][u] = 0
    else:
        graph[u][v] = 0
        graph[v][u] = 1

floyd()

k = int(sys.stdin.readline())

for _ in range(k):
    s, e = map(int, sys.stdin.readline().split())
    print(graph[s][e])
