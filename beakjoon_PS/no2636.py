import sys
import collections


def bfs(arr1, arr2, time, count):
    global N, M
    judge = False
    temp = 0
    for y in range(N):
        for x in range(M):
            if arr1[y][x] == 1:
                judge = True
                temp += 1

    if judge == False:
        print(time)
        print(count)

        return

    visited = [[False] * M for _ in range(N)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    queue = collections.deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        by, bx = queue.popleft()

        for i in range(4):
            ay = by + dy[i]
            ax = bx + dx[i]

            if ay >= 0 and ay < N and ax >= 0 and ax < M:
                if arr1[ay][ax] == 1:
                    arr2[ay][ax] = 0
                    visited[ay][ax] = True
                if arr1[ay][ax] == 0 and visited[ay][ax] == False:
                    visited[ay][ax] = True
                    queue.append((ay, ax))
    arr3 = []
    for i in arr2:
        arr3.append(i)

    bfs(arr2, arr3, time + 1, temp)


N, M = map(int, sys.stdin.readline().split())
arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr2 = []
for i in arr1:
    arr2.append(i)
bfs(arr1, arr2, 0, 0)
