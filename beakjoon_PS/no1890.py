import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            if i + arr[i][j] < n:
                dp[i+arr[i][j]][j] += dp[i][j]
            if j + arr[i][j] < n:
                dp[i][j+arr[i][j]] += dp[i][j]

print(dp[n-1][n-1])
