import sys


def backTracking(N, M, count, arr, checked, result):
    if count == M:
        return print(" ".join(map(str, result)))

    for i in range(N):
        if len(result) == 0:
            if checked[i] == False:
                result.append(arr[i])
                checked[i] = True
                backTracking(N, M, count+1, arr, checked, result)
                result.pop()
                checked[i] = False
        else:
            if checked[i] == False and result[-1] < arr[i]:
                result.append(arr[i])
                checked[i] = True
                backTracking(N, M, count+1, arr, checked, result)
                result.pop()
                checked[i] = False


N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
count = 0
checked = [False for _ in range(N)]
result = []
backTracking(N, M, count, arr, checked, result)
