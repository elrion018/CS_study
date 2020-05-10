import sys


def move(y, x, dy, dx):
    count = 0  # 이동한 칸수
    # 다음 이동이 벽이거나 구멍일 때까지
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        count += 1
    return y, x, count


def bfs():
    global visited_R, visited_B
    # 이동 좌표와 queue 선언
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]  # 서 동 북 남
    queue = []
    # 구슬 좌표 정보 선언
    Ry, Rx, By, Bx = [0]*4
    # 완전 탐색
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                Ry, Rx = i, j
            elif board[i][j] == 'B':
                By, Bx = i, j
    queue.append((Ry, Rx, By, Bx, 1))  # 위치정보와 depth까지
    visited_R[Ry][Rx] = True
    visited_B[By][Bx] = True
    while queue:
        Ry, Rx, By, Bx, depth = queue.pop(0)
        if depth > 10:  # 10 이하여야 한다.
            break
        for i in range(4):  # 4방향으로 시도
            next_Ry, next_Rx, R_count = move(Ry, Rx, dy[i], dx[i])  # red
            next_By, next_Bx, B_count = move(By, Bx, dy[i], dx[i])  # blue

            if board[next_By][next_Bx] == 'O':  # 파란 구슬이 구멍에 떨어졌다면 실패
                continue  # 아래 코드를 실행시키지 않고 되돌아감

            if board[next_Ry][next_Rx] == 'O':  # 빨간 구슬이 구멍에 떨어졌다면 성공
                print(1)
                return
            if next_Ry == next_By and next_Rx == next_Bx:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸 x
                if R_count > B_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    # 서 동 북 남
                    if i == 0:  # 서
                        next_Rx += 1
                    elif i == 1:  # 동
                        next_Rx -= 1
                    elif i == 2:  # 북
                        next_Ry += 1
                    elif i == 3:  # 남
                        next_Ry -= 1
                else:
                    if i == 0:  # 서
                        next_Bx += 1
                    elif i == 1:  # 동
                        next_Bx -= 1
                    elif i == 2:  # 북
                        next_By += 1
                    elif i == 3:  # 남
                        next_By -= 1
            # 방문 여부 확인
            if visited_R[next_Ry][next_Rx] == False or visited_B[next_By][next_Bx] == False:
                visited_R[next_Ry][next_Rx] = True
                visited_B[next_By][next_Bx] = True
                queue.append((next_Ry, next_Rx, next_By, next_Bx, depth + 1))
    print(0)


# 입력
N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(N)]

# 방문체크 배열 선언
visited_R = [[False]*M for _ in range(N)]
visited_B = [[False]*M for _ in range(N)]
bfs()
