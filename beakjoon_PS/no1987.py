import sys

maxVal = 1


def dfs(visited, y, x, result):
    global maxVal

    maxVal = max(result, maxVal)
    for i in range(4):
        ay = y + dy[i]
        ax = x + dx[i]
        if ay >= 0 and ax >= 0 and ay < R and ax < C:
            if not visited[ord(arr[ay][ax])-65]:
                visited[ord(arr[ay][ax])-65] = 1
                dfs(visited, ay, ax, result+1)
                visited[ord(arr[ay][ax])-65] = 0


R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [0] * 26
visited[ord(arr[0][0])-65] = 1
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


dfs(visited, 0, 0, 1)
print(maxVal)
