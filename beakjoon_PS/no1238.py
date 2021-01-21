import sys
import heapq


def init(st):
    dist = [inf] * (N+1)
    dist[st] = 0
    q = [[dist[st], st]]
    return dist, q


def Di(st, end):
    dist, q = init(st)

    while q:
        a = heapq.heappop(q)[1]
        if len(graph) > 0:
            for w, b in graph[a]:
                cal = dist[a] + w
                if dist[b] > cal:
                    dist[b] = cal
                    heapq.heappush(q, [dist[b], b])
    return dist[end]


N, M, X = map(int, sys.stdin.readline().split())
maxVal = -sys.maxsize
inf = sys.maxsize
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append([w, b])


for i in range(1, N+1):
    temp1 = Di(i, X)
    temp2 = Di(X, i)
    res = temp1 + temp2
    maxVal = max(maxVal, res)
print(maxVal)
