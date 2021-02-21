import sys

N, T = map(int, sys.stdin.readline().split())

arr = [[0]]
dp = [[0]*(T+1) for _ in range(N+1)]


for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, T+1):
        dp[i][j] = dp[i-1][j]
        if j - arr[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
print(max(dp[N]))
