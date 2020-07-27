import sys
import collections


def bfs(M, N, ripe):
    visited = [[0]*M for _ in range(N)]
    queue = collections.deque()
    for element in ripe:
        visited[element[0]][element[1]] = 1
        queue.append(element)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    last_visited = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < N and ax >= 0 and ax < M:
                if visited[ay][ax] == 0 and box[ay][ax] == 0:
                    visited[ay][ax] = visited[y][x] + 1
                    queue.append((ay, ax))
                    last_visited = visited[ay][ax]
    return judge(visited, last_visited, M, N)


def search_ripe(M, N):
    ripe = []
    unripe = 0
    for y in range(N):
        for x in range(M):
            if box[y][x] == 0:
                unripe += 1
            if box[y][x] == 1:
                ripe.append((y, x))
    if unripe == 0:
        print(0)
        sys.exit()
    return ripe


def judge(visited, last_visited, M, N):
    for y in range(N):
        for x in range(M):
            if visited[y][x] == 0 and box[y][x] == 0:
                return print(-1)
    return print(last_visited-1)


M, N = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ripe = search_ripe(M, N)
bfs(M, N, ripe)
