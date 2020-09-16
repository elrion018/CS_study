import sys
import collections
maxVal = -sys.maxsize


def temp(y, x, N, M):
    global maxVal
    sumVal = arr[y][x]
    if y == 0:
        if x == 0 or x == M-1:
            return
    elif y == N-1:
        if x == 0 or x == M-1:
            return
    if y == 0:
        sumVal = sumVal + arr[y][x-1] + arr[y][x+1] + arr[y+1][x]
    elif y == N-1:
        sumVal = sumVal + arr[y][x-1] + arr[y][x+1] + arr[y-1][x]
    elif x == 0:
        sumVal = sumVal + arr[y-1][x] + arr[y+1][x] + arr[y][x+1]
    elif x == M-1:
        sumVal = sumVal + arr[y-1][x] + arr[y+1][x] + arr[y][x-1]
    else:
        sumList = []
        sumList.append(sumVal + arr[y][x-1] + arr[y][x+1] + arr[y+1][x])
        sumList.append(sumVal + arr[y][x-1] + arr[y][x+1] + arr[y-1][x])
        sumList.append(sumVal + arr[y-1][x] + arr[y+1][x] + arr[y][x+1])
        sumList.append(sumVal + arr[y-1][x] + arr[y+1][x] + arr[y][x-1])
        sumVal = max(sumList)
    if maxVal < sumVal:
        maxVal = sumVal


def dfs(y, x, count, visited, sumVal):
    global maxVal
    if count == 4:
        if maxVal < sumVal:
            maxVal = sumVal
        return
    for i in range(4):
        ay = y + dy[i]
        ax = x + dx[i]
        if ay >= 0 and ay < N and ax >= 0 and ax < M:
            if visited[ay][ax] == False:
                visited[ay][ax] = True
                dfs(ay, ax, count+1, visited, sumVal + arr[ay][ax])
                visited[ay][ax] = False


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for y in range(N):
    for x in range(M):
        temp(y, x, N, M)
        visited[y][x] = True
        dfs(y, x, 1, visited, arr[y][x])
        visited[y][x] = False

print(maxVal)
