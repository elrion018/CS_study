import sys
import collections


def F_bfs():
    global visited
    q = collections.deque()
    q.append((f1, f2))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < R and ax >= 0 and ax < C:
                if arr[ay][ax] != "#" and arr[ay][ax] != "F" and (visited[y][x][0] + 1 < visited[ay][ax][0] or visited[ay][ax][0] == 0):
                    visited[ay][ax][0] = visited[y][x][0] + 1
                    q.append((ay, ax))


def J_bfs():
    global visited
    q = collections.deque()
    q.append((j1, j2))
    while q:
        y, x = q.popleft()
        if y == R - 1 or x == C - 1 or y == 0 or x == 0:
            return visited[y][x][1] + 1
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < R and ax >= 0 and ax < C:
                if arr[ay][ax] != "#" and arr[ay][ax] != "F" and arr[ay][ax] != "J" and visited[ay][ax][1] == 0:
                    if (visited[y][x][1] + 1 < visited[ay][ax][0] or visited[ay][ax][0] == 0):
                        visited[ay][ax][1] = visited[y][x][1] + 1
                        q.append((ay, ax))
    return "IMPOSSIBLE"


R, C = map(int, sys.stdin.readline().split())


arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
j1, j2 = 0, 0
f1, f2 = 0, 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visited = [[[0, 0] for _ in range(C)]for _ in range(R)]
for y in range(R):
    for x in range(C):
        if arr[y][x] == "J":
            j1, j2 = y, x
        elif arr[y][x] == "F":
            f1, f2 = y, x
            F_bfs()

print(J_bfs())
