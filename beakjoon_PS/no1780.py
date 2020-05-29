import sys
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0


def make_paper(y, x, N):
    global cnt_1, cnt_2, cnt_3
    check = paper[y][x]
    for i in range(y, N+y):
        for j in range(x, N+x):
            if paper[i][j] != check:
                make_paper(y, x, N//3)  # 1
                make_paper(y, x+N//3, N//3)  # 2
                make_paper(y, x+(N//3)*2, N//3)  # 3
                make_paper(y+N//3, x, N//3)  # 4
                make_paper(y+N//3, x+N//3, N//3)  # 5
                make_paper(y+N//3, x+(N//3)*2, N//3)  # 6
                make_paper(y+(N//3)*2, x, N//3)  # 7
                make_paper(y+(N//3)*2, x+N//3, N//3)  # 8
                make_paper(y+(N//3)*2, x+(N//3)*2, N//3)
                return
    if check == '-1':
        cnt_1 += 1
        return
    elif check == '0':
        cnt_2 += 1
        return
    elif check == '1':
        cnt_3 += 1
        return


N = int(sys.stdin.readline())
paper = [sys.stdin.readline().split() for _ in range(N)]

make_paper(0, 0, N)
print(cnt_1)
print(cnt_2)
print(cnt_3)
