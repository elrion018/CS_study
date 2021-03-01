import sys
import collections


def bfs(sty, stx):
    global ans_sheep, ans_wolf
    q = collections.deque()
    q.append([sty, stx])
    visited[sty][stx] = 1
    sheep = 0
    wolf = 0
    if arr[sty][stx] == 'v':
        wolf += 1
    elif arr[sty][stx] == 'o':
        sheep += 1
    while q:
        y, x = q.popleft()

        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < R and ax >= 0 and ax < C:
                if visited[ay][ax] == 0 and arr[ay][ax] != "#":
                    visited[ay][ax] = 1
                    q.append([ay, ax])
                    if arr[ay][ax] == 'v':
                        wolf += 1
                    elif arr[ay][ax] == 'o':
                        sheep += 1
    if sheep > wolf:
        ans_sheep += sheep

    else:
        ans_wolf += wolf

    return


R, C = map(int, sys.stdin.readline().split())

arr = []
for _ in range(R):
    arr.append(list(sys.stdin.readline().strip()))
visited = [[0]*C for _ in range(R)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

ans_sheep = 0
ans_wolf = 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and arr[i][j] != '#':
            bfs(i, j)
print(ans_sheep, ans_wolf)
