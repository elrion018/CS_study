import sys


def dfs(n, count, visited, y, x, now):
    global ans
    if count == n:
        ans += now
        return
    for i in range(4):
        ay = y + dy[i]
        ax = x + dx[i]
        if ay >= 0 and ay < 30 and ax >= 0 and ax < 30:
            if visited[ay][ax] != 1:
                visited[ay][ax] = 1
                dfs(n, count + 1, visited, ay, ax, now*per[i])
                visited[ay][ax] = 0


n, E, W, S, N = map(int, sys.stdin.readline().split())

per = [E/100, W/100, S/100, N/100]
visited = [[0]*30 for _ in range(30)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


ans = 0
visited[15][15] = 1
dfs(n, 0, visited, 15, 15, 1)

print("%0.11f" % ans)
