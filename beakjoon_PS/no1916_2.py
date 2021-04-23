import sys
import heapq

def init(start):
  inf = sys.maxsize
  dist = [inf] * (n+1)
  dist[start] = 0
  q = [[dist[start], start]]

  return dist, q

def di(start):
  dist, q = init(start)

  while q:
    now_dist, now = heapq.heappop(q)

    if dist[now] != now_dist:
      continue

    for node, w in adj[now]:
      cal = dist[now] + w

      if dist[node] > cal:
        dist[node] = cal
        heapq.heappush(q, [dist[node], node])

  return dist

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

adj = [[] for _ in range(n+1)]

for _ in range(m):
  st, end, weight = map(int, sys.stdin.readline().split())

  adj[st].append([end, weight])

start, end = map(int, sys.stdin.readline().split())
dist = di(start)

print(dist[end])