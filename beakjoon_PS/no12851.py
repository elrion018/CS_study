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
    return [0, 1]

  visited = [100000] * (2*max(start, destination)+1)
  q = collections.deque()
  min_time = sys.maxsize
  count = 0

  visited[start] = 0
  q.append(start)

  while q:
    x = q.popleft()

    for i in range(3):
      ax = cal(i, x)

      if ax >= 0 and ax < 2*max(start, destination)+1 and visited[ax] >= visited[x] + 1:
        visited[ax] = visited[x] + 1
        q.append(ax)

        if ax == destination:
          if min_time == visited[ax]:
            count += 1
          
          elif min_time > visited[ax]:
            min_time = visited[ax]
            count = 1

  return [min_time, count]

n, k = map(int, sys.stdin.readline().split())

ans = bfs(n,k)

print(ans[0])
print(ans[1])