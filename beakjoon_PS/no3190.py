#입력 (N, K, apple_loc, L, L_info)
N = int(input())
K = int(input())
apple_loc = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
L_info = [list(input().split()) for _ in range(L)]

# NxN 보드 생성 및 K개의 사과 배치
# 0 : 빈칸, 1: 뱀, 2:사과
board = [[0] * N for _ in range(N)]
for loc in apple_loc:
    board[loc[0]-1][loc[1]-1] = 2

# dx, dy 동, 남, 서, 북 순서 (오른쪽)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def rotate(direction, d):
    if direction == 'L':
        d -= 1
        if d == -1:
            d = 3

        return d
    elif direction == 'D':
        d += 1
        if d == 4:
            d = 0
        return d


def solve():
    # 머리, 꼬리 좌표, 시간, 방향 정보 저장용 리스트
    head = [0, 0]  # y,x 순
    tail = [0, 0]
    tail_queue = []
    count = 0
    d = 0
    # 시간 누적 및 방향 전환
    for info in L_info:
        # 방향 전환 시간까지 무한 반복
        while (count < int(info[0])):
            count += 1
            ay = head[0] + dy[d]
            ax = head[1] + dx[d]
            # 벽이나 자신의 몸에 닿지 않는다면
            if ax >= 0 and ax < N and ay >= 0 and ay < N and board[ay][ax] != 1:
                tail_queue.append(d)
                # 이동한 칸에 사과가 있다면
                if board[ay][ax] == 2:
                    board[ay][ax] = 0
                    board[ay][ax] = 1
                    head = [ay, ax]
                else:
                    board[ay][ax] = 1
                    board[tail[0]][tail[1]] = 0
                    head = [ay, ax]
                    temp = tail_queue.pop(0)
                    tail[0] = tail[0] + dy[temp]
                    tail[1] = tail[1] + dx[temp]
            else:
                return count
        # 방향 전환이 L이면 왼쪽 회전
        if info[1] == 'L':
            d = rotate('L', d)
        # D이면 오른쪽 회전
        else:
            d = rotate('D', d)
    while True:
        count += 1
        ay = head[0] + dy[d]
        ax = head[1] + dx[d]
        # 벽이나 자신의 몸에 닿지 않는다면
        if ax >= 0 and ax < N and ay >= 0 and ay < N and board[ay][ax] != 1:
            tail_queue.append(d)
            # 이동한 칸에 사과가 있다면
            if board[ay][ax] == 2:
                board[ay][ax] = 0
                board[ay][ax] = 1
                head = [ay, ax]
            else:
                board[ay][ax] = 1
                board[tail[0]][tail[1]] = 0
                head = [ay, ax]
                temp = tail_queue.pop(0)
                tail[0] = tail[0] + dy[temp]
                tail[1] = tail[1] + dx[temp]
        else:
            return count


print(solve())
