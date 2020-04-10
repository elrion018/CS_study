import sys


def backTracking(N, M, count, result):
    if count == M:
        print(" ".join(map(str, result)))
    for i in range(N):
        if checked[i] == False:
            result.append(i+1)
            checked[i] = True
            backTracking(N, M, count + 1, result)
            result.pop()
            checked[i] = False


N, M = map(int, sys.stdin.readline().split())
count = 0
checked = [False for i in range(N)]
result = []
backTracking(N, M, count, result)
