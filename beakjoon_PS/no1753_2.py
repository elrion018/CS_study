import sys
import heapq


def init(K):
    dist = [inf] * (V+1)
    dist[K] = 0
    q = [[dist[K], K]]

    return dist, q


def Di(K):
    dist, q = init(K)

    while q:
        a_dist, a = heapq.heappop(q)

        if dist[a] != a_dist:
          continue

        for b, w in arr[a]:
            cal = dist[a] + w
            if dist[b] > cal:
                dist[b] = cal
                heapq.heappush(q, [dist[b], b])

    return dist


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

inf = sys.maxsize

arr = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    arr[a].append([b, w])
dist = Di(K)
for i in range(1,len(dist)):
    if dist[i] == inf:
        print("INF")
    else:
        print(dist[i])
