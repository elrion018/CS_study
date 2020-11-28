import sys
import collections


def trans(visited):
    temp = []
    for i in range(len(visited)):
        if i % 2 != 0:
            temp.extend(visited[i][:-1])
        else:
            temp.extend(visited[i])

    return [0] + temp


def bfs():
    visited = [[0]*N for _ in range(N)]
    # dy1 = [0, 1, -1]  # 서 남 북
    # dx1 = [-1, -1, -1]
    dy1 = [1, 0, -1]  # 남 서 북
    dx1 = [-1, -1, -1]
    ##
    dy2 = [0, 1, -1]  # 동 남 북
    dx2 = [1, 0, 0]
    ##
    # dy3 = [0, 1, -1]  # 서 남 북
    # dx3 = [-1, 0, 0]
    dy3 = [1, 0, -1]
    dx3 = [0, -1, 0]
    ##
    dy4 = [0, 1, -1]  # 동 남 북
    dx4 = [1, 1, 1]
    q = collections.deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for idx in range(2):
            for i in range(3):
                if idx == 0 and y % 2 == 0:
                    ay = y + dy1[i]
                    ax = x + dx1[i]
                elif idx == 1 and y % 2 == 0:
                    ay = y + dy2[i]
                    ax = x + dx2[i]
                elif idx == 0 and y % 2 != 0:
                    ay = y + dy3[i]
                    ax = x + dx3[i]
                elif idx == 1 and y % 2 != 0:
                    ay = y + dy4[i]
                    ax = x + dx4[i]
                if ax >= 0 and ax < N and ay >= 0 and ay < N and arr[ay][ax] != 0:
                    if idx == 0:
                        if arr[y][x][idx] == arr[ay][ax][1] and visited[ay][ax] == 0:
                            q.append([ay, ax])
                            visited[ay][ax] = arr[y][x][2]
                    elif idx == 1:
                        if arr[y][x][1] == arr[ay][ax][0] and visited[ay][ax] == 0:
                            q.append([ay, ax])
                            visited[ay][ax] = arr[y][x][2]
    visited = trans(visited)
    hr = None
    for i in range(len(visited)-1, 0, -1):
        if visited[i] != 0:
            hr = i
            break
    result = []
    while hr != 1:
        result.append(hr)
        hr = visited[hr]
    result.append(1)
    result = list(reversed(result))
    print(len(result))

    for j in result:
        print(j, end=' ')
    return


N = int(sys.stdin.readline())

arr = [[0]*N for _ in range(N)]

y = 0
num = 1

for y in range(N):
    for x in range(N):
        if x == N-1 and y % 2 != 0:
            pass
        else:
            a, b = map(int, sys.stdin.readline().split())
            arr[y][x] = [a, b, num]
            num += 1
bfs()
