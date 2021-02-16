import sys


def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    graph[i][j] = 0
                elif i != k and j != k:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


N, M = map(int, sys.stdin.readline().split())

graph = [[sys.maxsize]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

floyd()


for i in range(len(graph)):
    graph[i] = [i+1, sum(graph[i])]
graph = sorted(graph, key=lambda ele: (ele[1], ele[0]))
print(graph[0][0])
