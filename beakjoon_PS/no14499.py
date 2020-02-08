
# 입력
N, M, x, y, K = map(int, input().split())

# 지도 입력값 받기
_map = [list(map(int, input().split())) for _ in range(N)]

# 명령 입력받기

orders = list(map(int, input().split()))

# 주사위 전개도

dice = [1, 2, 3, 4, 5, 6]

# 주사위 면에 있는 정수들

ints = [0, 0, 0, 0, 0, 0]


def solve(orders, x, y):
    # 주사위 이동
    for order in orders:
        # 주사위 전개도 내용 복사
        temp = dice[:]
        if order == 1:  # 동
            if x + 1 >= 0 and x + 1 < M:
                # 전개도 변형
                dice[0] = temp[3]
                dice[3] = temp[5]
                dice[5] = temp[2]
                dice[2] = temp[0]
                # x, y 좌표 이동(주사위 이동)
                x += 1
                judge(x, y)
        elif order == 2:  # 서
            if x - 1 >= 0 and x - 1 < M:
                dice[0] = temp[2]
                dice[2] = temp[5]
                dice[5] = temp[3]
                dice[3] = temp[0]
                x -= 1
                judge(x, y)
        elif order == 3:  # 북
            if y - 1 >= 0 and y - 1 < N:
                dice[0] = temp[1]
                dice[1] = temp[5]
                dice[5] = temp[4]
                dice[4] = temp[0]
                y -= 1
                judge(x, y)
        elif order == 4:  # 남
            if y + 1 >= 0 and y + 1 < N:
                dice[0] = temp[4]
                dice[4] = temp[5]
                dice[5] = temp[1]
                dice[1] = temp[0]
                y += 1
                judge(x, y)


def judge(x, y):
    if _map[y][x] == 0:
        copy_num_in_dice(x, y)

    else:
        copy_num_in_map(x, y)


def copy_num_in_map(x, y):
    ints[dice[5]-1] = _map[y][x]
    _map[y][x] = 0
    print(ints[dice[0]-1])


def copy_num_in_dice(x, y):
    _map[y][x] = ints[dice[5]-1]
    print(ints[dice[0]-1])


solve(orders, y, x)
