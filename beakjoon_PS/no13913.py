import sys
import collections

def cal(i, x):
  if i == 0:
    return x - 1

  elif i == 1:
    return x + 1
  
  elif i == 2:
    return 2 * x


def bfs(start, destination):
  if start == destination:
    return [0, [start]]

  visited = [[100000, None] for _ in range(2*max(start, destination)+1)]
  q = collections.deque()
  min_time = sys.maxsize

  visited[start] = [0, None]
  q.append(start)

  while q:
    x = q.popleft()

    for i in range(3):
      ax = cal(i, x)

      if ax >= 0 and ax < 2*max(start, destination)+1 and visited[ax][0] >= visited[x][0] + 1:
        visited[ax][0] = visited[x][0] + 1
        visited[ax][1] = x
        q.append(ax)

        if ax == destination:
          if min_time > visited[ax][0]:
            min_time = visited[ax][0]

  trace = []
  vertex = destination

  while True:
    trace.append(vertex)

    if visited[vertex][1] == None:
      break

    vertex = visited[vertex][1]

  trace.reverse()

  return [min_time, trace]

n, k = map(int, sys.stdin.readline().split())

ans = bfs(n,k)

print(ans[0])
print(" ".join(list(map(str,ans[1]))))