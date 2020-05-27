import sys
blue = 0
white = 0


def make_paper(y, x, N):
    global paper, blue, white
    color = paper[y][x]
    for i in range(y, y+N):
        for j in range(x, x+N):
            if paper[i][j] != color:
                make_paper(y, x, N//2)  # 1
                make_paper(y, x+N//2, N//2)  # 2
                make_paper(y+N//2, x, N//2)  # 3
                make_paper(y+N//2, x+N//2, N//2)  # 4
                return
    if color == 1:
        blue += 1
        return
    else:
        white += 1
        return


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
make_paper(0, 0, N)
print(white)
print(blue)
