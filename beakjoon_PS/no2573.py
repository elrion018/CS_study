# 입력

N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

# dy, dx 선언 동 서 남 북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


# 얼음 녹이기 위한 반복문 실행
time = 0  # 시간을 누적할 변수 선언
count = 0
maxHeight = None
judge = False
while True:
    if count > 1:
        judge = True
        break
    if maxHeight == 0:
        break
    maxHeight = 0
    count = 0
    time += 1
    temp = [sea[i].copy() for i in range(N)]
    # 얼음 녹이기
    for y in range(N):
        for x in range(M):
            if sea[y][x] != 0:
                for i in range(4):
                    ay = y + dy[i]
                    ax = x + dx[i]
                    if temp[ay][ax] == 0 and sea[y][x] != 0:
                        sea[y][x] -= 1
                        if maxHeight < sea[y][x]:
                            maxHeight = sea[y][x]
                    else:
                        if maxHeight < sea[y][x]:
                            maxHeight = sea[y][x]
    # bfs 하기
    visited = [[0]*M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if sea[y][x] != 0 and visited[y][x] != 1:
                visited[y][x] = 1
                queue = [[y, x]]
                while True:
                    if len(queue) == 0:
                        break
                    queue_y, queue_x = queue.pop(0)
                    for i in range(4):
                        ay = queue_y + dy[i]
                        ax = queue_x + dx[i]
                        if ax >= 0 and ay >= 0 and ax < M and ay < N and sea[ay][ax] != 0 and visited[ay][ax] != 1:
                            visited[ay][ax] = 1
                            queue.append([ay, ax])
                count += 1

if judge == True:
    print(time)
else:
    print(0)
