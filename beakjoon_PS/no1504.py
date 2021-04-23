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

    for next, weight in adj[now]:
      cal = dist[now] + weight

      if dist[next] > cal:
          dist[next] = cal
          heapq.heappush(q, [dist[next], next])

  return dist


n, e = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, sys.stdin.readline().split())

  adj[a].append([b, c])
  adj[b].append([a, c])

stopover1, stopover2 = map(int, sys.stdin.readline().split())

dist1 = di(1)
dist2 = di(stopover1)
dist3 = di(stopover2)

answer = min(dist1[stopover1] + dist2[stopover2] + dist3[n], dist1[stopover2] + dist3[stopover1] + dist2[n])

if answer >= sys.maxsize:
  print(-1)

else:
  print(answer)