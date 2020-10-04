import sys


def dfs(visited, y, count, val):
    global maxVal
    if count == 11:
        if maxVal < val:
            maxVal = val
        return

    for x in range(11):
        if arr[y][x] != 0 and visited[x] == False:
            visited[x] = True
            dfs(visited, y+1, count+1, val + arr[y][x])
            visited[x] = False


C = int(sys.stdin.readline())
maxVal = -sys.maxsize
for _ in range(C):
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    maxVal = -sys.maxsize
    visited = [False for _ in range(11)]
    dfs(visited, 0, 0, 0)
    print(maxVal)
