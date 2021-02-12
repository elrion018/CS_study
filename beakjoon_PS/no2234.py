import sys
# import collections
n, m = map(int, sys.stdin.readline().split())


def dfs(sy, sx, cnt):
    stack = [[sy, sx]]
    visited[sy][sx] = cnt

    res = 1
    while stack:

        y, x = stack.pop()
        # 동
        if arr[y][x] & 4 == 0:
            ay = y + dy[0]
            ax = x + dx[0]
            if ay >= 0 and ay < m and ax >= 0 and ax < n and visited[ay][ax] == 0:
                visited[ay][ax] = cnt
                res += 1
                stack.append([ay, ax])
        # 서
        if arr[y][x] & 1 == 0:
            ay = y + dy[1]
            ax = x + dx[1]
            if ay >= 0 and ay < m and ax >= 0 and ax < n and visited[ay][ax] == 0:
                visited[ay][ax] = cnt
                res += 1
                stack.append([ay, ax])
        # 남
        if arr[y][x] & 8 == 0:
            ay = y + dy[2]
            ax = x + dx[2]
            if ay >= 0 and ay < m and ax >= 0 and ax < n and visited[ay][ax] == 0:
                visited[ay][ax] = cnt
                res += 1
                stack.append([ay, ax])
        # 북
        if arr[y][x] & 2 == 0:
            ay = y + dy[3]
            ax = x + dx[3]
            if ay >= 0 and ay < m and ax >= 0 and ax < n and visited[ay][ax] == 0:
                visited[ay][ax] = cnt
                res += 1
                stack.append([ay, ax])
    table.append(res)
    return


arr = []
table = [0]
maxVal = -sys.maxsize
visited = [[0]*n for _ in range(m)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for _ in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))
cnt = 1
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, cnt)
            cnt += 1
# print(visited)
# print(table)

for i in range(m):
    for j in range(n):
        for k in range(4):
            ay = i + dy[k]
            ax = j + dx[k]
            if ay >= 0 and ay < m and ax >= 0 and ax < n:
                if visited[i][j] != visited[ay][ax]:
                    maxVal = max(
                        maxVal, table[visited[i][j]] + table[visited[ay][ax]])
print(len(table)-1)
print(max(table))
print(maxVal)
