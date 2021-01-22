import sys


def floyd(N):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    graph[i][j] = 0
                elif i != k and j != k:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    temp = []
    for i in range(1, len(graph)):
        temp.append(graph[i][1:])
    return temp


N = int(sys.stdin.readline())
inf = sys.maxsize

graph = [[inf] * (N+1) for _ in range(N+1)]

a, b = None, None
while a != -1 and b != -1:
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

graph = floyd(N)
minVal = sys.maxsize
for i in range(len(graph)):
    temp = max(graph[i])
    graph[i] = temp
    minVal = min(minVal, temp)

cnt = 0
res = []
for i in range(len(graph)):
    if graph[i] == minVal:
        cnt += 1
        res.append(i+1)
res = sorted(res)
print(minVal, cnt)
for i in res:
    print(i, end=' ')
