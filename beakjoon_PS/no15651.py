import sys


def backTracking(N, M, count, result):
    if M == count:
        return print(" ".join(map(str, result)))
    for i in range(1, N+1):
        result.append(i)

        backTracking(N, M, count+1, result)
        result.pop()


N, M = map(int, sys.stdin.readline().split())
count = 0
result = []
backTracking(N, M, count, result)
