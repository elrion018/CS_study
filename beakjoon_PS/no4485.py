import sys
import heapq


def init(stY, stX):
    dist = [[inf] * N for _ in range(N)]
    dist[stY][stX] = graph[stY][stX]
    q = [[dist[stY][stX], [stY, stX]]]

    return dist, q


def Di(stY, stX):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    dist, q = init(stY, stX)

    while q:
        y, x = heapq.heappop(q)[1]
        # print(y, x)
        for i in range(4):
            ay = dy[i] + y
            ax = dx[i] + x
            if ay >= 0 and ay < N and ax >= 0 and ax < N:
                cal = dist[y][x] + graph[ay][ax]
                if dist[ay][ax] > cal:
                    dist[ay][ax] = cal
                    heapq.heappush(q, [dist[ay][ax], [ay, ax]])

    return dist[N-1][N-1]


inf = sys.maxsize
cnt = 0
while True:
    cnt += 1
    N = int(sys.stdin.readline())
    if N == 0:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print("Problem %d:" % cnt, end=' ')
    print(Di(0, 0))
