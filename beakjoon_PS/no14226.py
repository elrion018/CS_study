import sys, collections



s = int(sys.stdin.readline())

check = [[-1] * 1001 for _ in range(1001)]

q = collections.deque()

q.append([1, 0])

check[1][0] = 0

ans = sys.maxsize
while q:
  y, x = q.popleft()
  # 복사
  if check[y][y] == -1:
    check[y][y] = check[y][x] + 1
    q.append([y,y])

  #붙여넣기
  if y+x <= s and check[y+x][x] == -1:
    check[y+x][x] = check[y][x] + 1
    q.append([y+x, x])

  #삭제
  if y - 1 >= 0 and check[y-1][x] == -1:
    check[y-1][x] = check[y][x] + 1
    q.append([y-1, x])

for i in range(len(check[s])):
  if check[s][i] != -1 and check[s][i] < ans:
    ans = check[s][i]
print(ans)