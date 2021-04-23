import sys, heapq

def init(start):
  inf = sys.maxsize
  times = [inf] * n
  times[start] = 0
  q = [[times[start], start]]

  return times, q

def di(start):
  times, q = init(start)

  while q:
    now_time, now = heapq.heappop(q)

    if times[now] != now_time:
      continue

    for next, time in adj[now]:
      cal = times[now] + time

      if times[next] > cal:
        times[next] = cal
        heapq.heappush(q, [times[next], next])

  return times

n, m = map(int, sys.stdin.readline().split())
companies = []

for _ in range(n):
  companies.append(int(sys.stdin.readline()))

subway_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

adj = [[] for _ in range(n)]

for i in range(n):
  for j in range(n):
    if subway_map[i][j] != 0:
      if companies[i] != companies[j]:
        adj[i].append([j, subway_map[i][j] + 10**6])
        adj[j].append([i, subway_map[i][j] + 10**6])

      else:
        adj[i].append([j, subway_map[i][j]])
        adj[j].append([i, subway_map[i][j]])

times = di(0)

print(times[m] // 10 ** 6 , times[m] % 10**6)