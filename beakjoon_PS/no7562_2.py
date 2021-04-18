import sys, collections

def bfs(visited, start_y, start_x, end_y, end_x):
  q = collections.deque()
  q.append([start_y, start_x])
  visited[start_y][start_x] = 1

  dy = [-1, -2, -2, -1, 1, 2, 2, 1]
  dx = [-2, -1, 1, 2, 2, 1, -1, -2]

  while q:
    by, bx = q.popleft()

    if by == end_y and bx == end_x:
      
      return visited[by][bx] 

    for i in range(8):
      ay = by + dy[i]
      ax = bx + dx[i]

      if ay >= 0 and ay < l and ax >= 0 and ax <l and visited[ay][ax] == 0:
        q.append([ay, ax])
        visited[ay][ax] = visited[by][bx] + 1

t = int(sys.stdin.readline())

for _ in range(t):
  l = int(sys.stdin.readline())
  visited = [[0] * l for _ in range(l)]
  start_y, start_x = map(int, sys.stdin.readline().split())
  end_y, end_x = map(int, sys.stdin.readline().split())

  print(bfs(visited, start_y, start_x, end_y, end_x)-1)
