import sys


def floyd(arr):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    arr[i][j] = 0
                elif arr[i][j] == 1 or (arr1[i][k] == 1 and arr[k][j] == 1):
                    arr[i][j] = 1
    temp = []
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == inf:
                arr[i][j] = 0
        temp.append(arr[i][1:])
    return temp


N, M = map(int, sys.stdin.readline().split())

inf = sys.maxsize

arr1 = [[inf] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr1[a][b] = 1


arr1 = floyd(arr1)

ans = 0

for i in range(N):
    judge = 0
    for j in range(N):
        judge += arr1[i][j] + arr1[j][i]
    if judge == N-1:
        ans += 1
print(ans)
