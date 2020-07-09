import sys
import collections


def bfs():
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    queue = collections.deque()
    visited[0][0][0] = 1
    queue.append((0, 0, 0))
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    while queue:
        y, x, z = queue.popleft()
        if y == N-1 and x == M-1:
            return print(visited[y][x][z])

        for i in range(4):
            ay = y+dy[i]
            ax = x+dx[i]
            if ay >= 0 and ay < N and ax >= 0 and ax < M and visited[ay][ax][z] == 0:
                if arr[ay][ax] == '0':
                    visited[ay][ax][z] = visited[y][x][z] + 1
                    queue.append((ay, ax, z))
                elif arr[ay][ax] == '1' and z == 0:
                    visited[ay][ax][1] = visited[y][x][z] + 1
                    queue.append((ay, ax, 1))
    return print(-1)


N, M = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
bfs()
