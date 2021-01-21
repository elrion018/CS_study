import sys
import collections


def bfs(y, x):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visited[y][x] = 1
    q = collections.deque()
    q.append([y, x])
    na = [[y, x]]
    mean = arr[y][x]
    while q:
        # print(q)
        y, x = q.popleft()

        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < N and ax >= 0 and ax < N:
                if visited[ay][ax] == 0 and abs(arr[ay][ax] - arr[y][x]) >= L and abs(arr[ay][ax] - arr[y][x]) <= R:
                    visited[ay][ax] = 1
                    q.append([ay, ax])
                    na.append([ay, ax])
                    mean += arr[ay][ax]
    return na, (mean // len(na))


N, L, R = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

res = 0

while True:
    visited = [[0]*N for _ in range(N)]
    # print("---")
    cnt = 0

    for y in range(N):
        for x in range(N):

            if visited[y][x] == 0:
                na, mean = bfs(y, x)
                if len(na) > 1:
                    cnt += 1
                    for ay, ax in na:
                        arr[ay][ax] = mean

    if cnt == 0:
        break
    else:
        res += 1
print(res)
