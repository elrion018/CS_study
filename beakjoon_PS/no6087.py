import sys
import collections


def bfs(fy, fx, ly, lx):
    global H, W, minVal
    visited = [[sys.maxsize]*W for _ in range(H)]
    queue = collections.deque()
    queue.append((fy, fx, 0))
    visited[fy][fx] = 0
    dy = [-1, 0, 1, 0]  # 북 동 남 서
    dx = [0, 1, 0, -1]

    y, x, count = queue.popleft()
    for i in range(4):
        ay = y + dy[i]
        ax = x + dx[i]
        if ay >= 0 and ay < H and ax >= 0 and ax < W:
            if (arr[ay][ax] == '.' or arr[ay][ax] == 'C') and visited[ay][ax] >= count:
                visited[ay][ax] = 0
                queue.append((ay, ax, 0, i))
    while queue:
        y, x, count, d = queue.popleft()
        if y == ly and x == lx:
            minVal = min(minVal, count)
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if i != d:
                if ay >= 0 and ay < H and ax >= 0 and ax < W:
                    if arr[ay][ax] != "*" and visited[ay][ax] >= count + 1:
                        visited[ay][ax] = count + 1
                        queue.append((ay, ax, count+1, i))

            else:
                if ay >= 0 and ay < H and ax >= 0 and ax < W:
                    if arr[ay][ax] != "*" and visited[ay][ax] >= count:
                        visited[ay][ax] = count
                        queue.append((ay, ax, count, i))


W, H = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(H)]
minVal = sys.maxsize
temp = []
for y in range(H):
    for x in range(W):
        if arr[y][x] == 'C':
            temp.append((y, x))
bfs(temp[0][0], temp[0][1], temp[1][0], temp[1][1])
print(minVal)
