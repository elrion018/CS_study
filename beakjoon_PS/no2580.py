import sys


def horizontal(y, val):
    if val in sudoku[y]:
        return False
    return True


def vertical(x, val):
    for i in range(9):
        if val == sudoku[i][x]:
            return False
    return True


def bythree(y, x, val):
    nx = (x//3) * 3
    ny = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[ny+i][nx+j]:
                return False
    return True


def backTracking(index):
    global zeros
    if index == len(zeros):
        for row in sudoku:
            for i in row:
                print(i, end=" ")
            print()
        return sys.exit(0)

    else:
        for i in range(1, 10):
            nx = zeros[index][1]
            ny = zeros[index][0]

            if horizontal(ny, i) and vertical(nx, i) and bythree(ny, nx, i):
                sudoku[ny][nx] = i
                backTracking(index+1)
                sudoku[ny][nx] = 0


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))
backTracking(0)
