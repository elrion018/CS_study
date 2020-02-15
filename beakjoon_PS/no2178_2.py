# 입력

N, M = map(int, input().split())

# 미궁과 방문내역 선언
maze = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

visited[0][0] = 1

for i in range(N):
    temp = input()
    for j in range(M):
        maze[i][j] = int(temp[j])


# queue 선언
queue = [[0, 0]]

# 동서남북 좌표계 선언
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solve():

    while True:

        # queue에서 좌표 꺼내기
        x, y = queue.pop(0)

        # (N, M)에 도달했다면 종료
        if x == M-1 and y == N-1:
            break

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            # 미로를 벗어나거나 벽에 해당하지 않는가 그리고 이전에 방문한적 없는가
            if ay >= 0 and ay < N and ax >= 0 and ax < M and maze[ay][ax] != 0 and visited[ay][ax] != 1:
                maze[ay][ax] = maze[y][x] + 1
                visited[ay][ax] = 1
                queue.append([ax, ay])

    return maze[N-1][M-1]


print(solve())
