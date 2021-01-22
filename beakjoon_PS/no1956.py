import sys


def floyd():
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if i == j:
                    graph[i][j] = 0
                elif i != k and j != k:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    temp = []
    for i in range(1, len(graph)):
        temp.append(graph[i][1:])
    return temp


V, E = map(int, sys.stdin.readline().split())

inf = sys.maxsize

graph = [[inf] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
graph = floyd()
minVal = sys.maxsize
for i in range(len(graph)):
    for j in range(len(graph)):
        if i != j:
            minVal = min(minVal, graph[i][j] + graph[j][i])

if minVal == inf:
    print(-1)
else:
    print(minVal)
