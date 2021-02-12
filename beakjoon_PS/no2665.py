import sys
import heapq


def init():
    inf = sys.maxsize
    q = []
    dist = [inf] * (n*n)
    dist[0] = 0
    heapq.heappush(q, [dist[0], 0])

    return dist, q


def Di(end, graph):
    dist, q = init()
    while q:
        a = heapq.heappop(q)[1]
        if len(graph[a]) > 0:
            for i in range(len(graph[a])):
                cal = dist[a] + graph[a][i][0]
                # print(cal)
                if cal < dist[graph[a][i][1]]:
                    dist[graph[a][i][1]] = cal
                    heapq.heappush(q, [dist[graph[a][i][1]], graph[a][i][1]])
    # print(dist)
    # print(end)
    return dist[end]


n = int(sys.stdin.readline())

graph = [[] for _ in range(n*n)]


arr = []

for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

cnt = -1
# print(arr)
for y in range(n):
    for x in range(n):
        cnt += 1
        for k in range(4):
            ay = y + dy[k]
            ax = x + dx[k]
            if ay >= 0 and ay < n and ax >= 0 and ax < n:
                if arr[ay][ax] == "1":
                    graph[cnt].append([0, ay*n + ax])
                else:
                    graph[cnt].append([1, ay*n + ax])

print(Di(n*n - 1, graph))
