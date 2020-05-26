import sys
import collections
N, M, K = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline())[:-1]for _ in range(N)]
visited = [[[[0, 0]]*(K+1) for _ in range(M)] for _ in range(N)]
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def bfs():
    queue = collections.deque()
    queue.append((0, 0, 0, 0))
    visited[0][0][0][0] = 1
    while queue:
        y, x, z, q = queue.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][z][q]
        for i in range(4):
            ay, ax = y+dy[i], x+dx[i]
            if ay >= 0 and ay < N and ax >= 0 and ax < M and visited[ay][ax][z][q] == 0:
                if arr[ay][ax] == '0':
                    if q == 0:
                        visited[ay][ax][z][1] = visited[y][x][z][0] + 1
                        queue.append((ay, ax, z, 1))
                    else:
                        visited[ay][ax][z][0] = visited[y][x][z][1] + 1
                        queue.append((ay, ax, z, 0))
                if arr[ay][ax] == '1' and z+1 <= K:
                    if q == 0:
                        visited[ay][ax][z+1][1] = visited[y][x][z][0] + 1
                        queue.append((ay, ax, z+1, 1))
                    else:
                        visited[y][x][z][0] += visited[y][x][z][1] + 1
                        queue.append((y, x, z, 0))
    return -1


print(bfs())
