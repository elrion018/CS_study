
def solve():
    global result
    for i in range(N - 7):
        for j in range(M - 7):

            count1, count2 = 0, 0
            for k in range(i, i+8):
                for l in range(j, j+8):

                    # 맨 상단 왼쪽이 W으로 시작할 때

                    if (k+l-i-j) % 2 == 0:
                        if board[k][l] == 'B':
                            count1 += 1

                    else:
                        if board[k][l] == 'W':
                            count1 += 1
                    # 맨 상단 왼쪽이 B으로 시작할 때
                    if (k+l-i-j) % 2 == 0:
                        if board[k][l] == 'W':
                            count2 += 1

                    else:
                        if board[k][l] == 'B':
                            count2 += 1

            count3 = 0

            if count1 > count2:
                count3 = count2

            else:
                count3 = count1

            if result is None:
                result = count3

            else:
                if result > count3:
                    result = count3

    return result


# 입력
N, M = map(int, input().split())

board = [list(input()) for i in range(N)]

result = None

print(solve())
