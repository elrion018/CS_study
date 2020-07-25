import sys
import collections


def bfs(y, x, w, h, visited, arr):
    queue = collections.deque()
    queue.append((y, x))
    visited[y][x] = True

    dy = (0, 0, 1, -1, -1, -1, 1, 1)
    dx = (1, -1, 0, 0, 1, -1, 1, -1)

    while queue:
        y, x = queue.pop()
        for i in range(8):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < h and ax >= 0 and ax < w:
                if visited[ay][ax] == False and arr[ay][ax] == 1:
                    visited[ay][ax] = True
                    queue.append((ay, ax))
    return visited


def search(w, h, arr):
    visited = [[False]*w for _ in range(h)]
    temp = 0
    for y in range(h):
        for x in range(w):
            if visited[y][x] == False and arr[y][x] == 1:
                temp += 1
                visited = bfs(y, x, w, h, visited, arr)
    return temp


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    result = search(w, h, arr)
    print(result)
