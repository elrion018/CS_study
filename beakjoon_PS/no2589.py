import sys
import collections


def dfs(i, j):
    global maxVal
    visited = [[-1] * m for _ in range(n)]
    visited[i][j] = 0
    q = collections.deque()
    q.append([i, j])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < n and ax >= 0 and ax < m and arr[ay][ax] == 'L' and visited[ay][ax] == -1:
                visited[ay][ax] = visited[y][x] + 1
                maxVal = max(maxVal, visited[ay][ax])
                q.append([ay, ax])
    # print(visited)
    return


n, m = map(int, sys.stdin.readline().split())

arr = []
maxVal = -sys.maxsize
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            dfs(i, j)
print(maxVal)
