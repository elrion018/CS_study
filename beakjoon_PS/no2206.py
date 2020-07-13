import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline())[:-1]for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def bfs():
    queue = [(0, 0, 0)]
    visited[0][0][0] = 1
    while queue:
        y, x, z = queue.pop(0)
        if y == N-1 and x == M-1:
            return visited[y][x][z]
        for i in range(4):
            ay, ax = y+dy[i], x+dx[i]
            if ay >= 0 and ay < N and ax >= 0 and ax < M and visited[ay][ax][z] == 0:
                if arr[ay][ax] == '0':
                    visited[ay][ax][z] = visited[y][x][z] + 1
                    queue.append((ay, ax, z))
                if arr[ay][ax] == '1' and z == 0:
                    visited[ay][ax][1] = visited[y][x][z] + 1
                    queue.append((ay, ax, 1))

    return -1


print(bfs())
print(visited)
