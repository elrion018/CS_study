import sys


def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    graph[i][j] = 0
                elif i != k and j != k:
                    graph[i][j] = min(
                        graph[i][j], graph[i][k] + graph[k][j])
    temp = []
    for i in range(1, len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == inf:
                graph[i][j] = 0
        temp.append(graph[i][1:])
    return temp


n = int(sys.stdin.readline())
inf = sys.maxsize

graph = [[inf] * (n+1) for _ in range(n+1)]

m = int(sys.stdin.readline())

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)
graph = floyd()


for i in range(len(graph)):
    print(" ".join(list(map(str, graph[i]))))
