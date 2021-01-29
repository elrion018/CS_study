import sys


def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    graph[i][j] = 0
                elif i != k and j != k:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


N = int(sys.stdin.readline())

inf = sys.maxsize

graph = [[inf for _ in range(N+1)] for _ in range(N+1)]

M = int(sys.stdin.readline())

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1

floyd()

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i == j:
            pass
        else:
            if graph[i][j] == inf and graph[j][i] == inf:
                cnt += 1
    print(cnt)
