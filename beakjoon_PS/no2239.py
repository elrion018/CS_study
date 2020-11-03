import sys


def vertical(x, val):
    for i in range(9):
        if arr[i][x] == val:
            return False
    return True


def horizontal(y, val):
    if val in arr[y]:
        return False
    return True


def byThree(y, x, val):
    ay = (y//3) * 3
    ax = (x//3) * 3
    for i in range(3):
        for j in range(3):
            if arr[ay+i][ax+j] == val:
                return False
    return True


def BT(index):
    global results
    if index == len(zeros):
        for row in arr:
            for i in row:
                print(i, end="")
            print()
        return sys.exit(0)
    else:
        for val in range(1, 10):
            ay = zeros[index][0]
            ax = zeros[index][1]
            if vertical(ax, val) and horizontal(ay, val) and byThree(ay, ax, val):
                arr[ay][ax] = val
                BT(index+1)
                arr[ay][ax] = 0


arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]

zeros = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zeros.append((i, j))
BT(0)
