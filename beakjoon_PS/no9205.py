import sys


def dist(i, j):
    i_x = arr2[i][0]
    i_y = arr2[i][1]
    j_x = arr2[j][0]
    j_y = arr2[j][1]

    res = abs(i_x - j_x) + abs(i_y - j_y)
    return res


def floyd():
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if i == j:
                    continue
                if i != k and j != k:
                    arr1[i][j] = min(arr1[i][j], arr1[i][k] + arr1[k][j])


T = int(sys.stdin.readline())


for _ in range(T):
    n = int(sys.stdin.readline())
    inf = sys.maxsize
    arr1 = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i != j:
                arr1[i][j] = inf

    arr2 = [0] * (n+2)
    for i in range(n+2):
        arr2[i] = list(map(int, sys.stdin.readline().split()))

    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue

            if dist(i, j) <= 1000:
                arr1[i][j] = 1
    floyd()

    if arr1[0][n+1] > 0 and arr1[0][n+1] < inf:
        print("happy")
    else:
        print("sad")
