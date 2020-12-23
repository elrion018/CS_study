import sys

M, N = map(int, sys.stdin.readline().split())

arr1 = []  # 그리드
arr2 = []  # 1차원 배열

for _ in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    arr1.append(row)

for y in range(M):
    for x in range(N):
        arr2.append([y, x, arr1[y][x]])
arr2 = sorted(arr2, key=lambda ele: -ele[2])

dp = [[0]*N for _ in range(M)]
dp[0][0] = 1
for y, x, high in arr2:
    if x+1 < N and arr1[y][x+1] > high:
        dp[y][x] += dp[y][x+1]
    if x-1 >= 0 and arr1[y][x-1] > high:
        dp[y][x] += dp[y][x-1]
    if y+1 < M and arr1[y+1][x] > high:
        dp[y][x] += dp[y+1][x]
    if y-1 >= 0 and arr1[y-1][x] > high:
        dp[y][x] += dp[y-1][x]
print(dp[M-1][N-1])
