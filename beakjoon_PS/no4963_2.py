import sys, collections

def bfs(arr, visited, sty, stx, w, h):
  q = collections.deque()
  q.append([sty, stx])
  visited[sty][stx] = 1
  dy = [0, 0, 1, -1, -1, -1, 1, 1]
  dx = [1, -1, 0, 0, -1, 1, -1, 1]
  count = 1

  while q:
    by, bx = q.popleft()

    for i in range(8):
      ay = by + dy[i]
      ax = bx + dx[i]


      if ay >= 0 and ay < h and ax >= 0 and ax < w:
        if arr[ay][ax] == 1 and visited[ay][ax] == 0:
          q.append([ay, ax])
          visited[ay][ax] = 1

  return [count, visited]


while True:
  temp = list(map(int,sys.stdin.readline().split()))

  if temp[0] == 0:
    break

  w, h = temp[0], temp[1]
  count = 0
  arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
  visited = [[0]* w for _ in range(h)]
  
  for y in range(h):
    for x in range(w):
      if arr[y][x] == 1 and visited[y][x] == 0:
        results = bfs(arr, visited, y, x, w, h)
        count += results[0]
        visited = results[1]

  print(count)

