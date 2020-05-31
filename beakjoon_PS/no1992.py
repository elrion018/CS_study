import sys


def quadtree(y, x, N):
    num = screen[y][x]
    for i in range(y, y+N):
        for j in range(x, x+N):
            if screen[i][j] != num:
                print('(', end='')
                quadtree(y, x, N//2)  # 1
                quadtree(y, x+N//2, N//2)  # 2
                quadtree(y+N//2, x, N//2)  # 3
                quadtree(y+N//2, x+N//2, N//2)  # 4
                return print(')', end='')

    if num == '1':
        return print('1', end='')
    else:
        return print('0', end='')


N = int(sys.stdin.readline())
screen = [list(sys.stdin.readline()) for _ in range(N)]
quadtree(0, 0, N)
