import sys
import heapq


def init(st):
    dist = dict()
    q = []
    for i in range(1, N*M + 1):
        if i == st:
            dist[i] = 0
        else:
            dist[i] = inf
    heapq.heappush(q, (dist[st], st))
    return dist, q


def Di(graph, st, end):
    dist, q = init(st)

    while q:
        a = heapq.heappop(q)[1]

        if len(graph[a]) > 1:
            for i in range(1, len(graph[a])):
                cal = dist[a]+graph[a][i][0]
                if cal < dist[graph[a][i][1]]:
                    dist[graph[a][i][1]] = cal
                    heapq.heappush(q, (dist[graph[a][i][1]], graph[a][i][1]))

    return dist[end]


M, N = map(int, sys.stdin.readline().split())

arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

inf = sys.maxsize

graph = [[0] for _ in range(N*M + 1)]
cnt = 0
for i in range(int(N)):
    for j in range(int(M)):

        cnt += 1
        for k in range(4):
            ay = i + dy[k]
            ax = j + dx[k]
            if ay >= 0 and ay < N and ax >= 0 and ax < M:
                if arr[ay][ax] == 1:
                    graph[cnt].append([1, ay*M + ax+1])
                else:
                    graph[cnt].append([0, ay*M + ax+1])

print(Di(graph, 1, N*M))
