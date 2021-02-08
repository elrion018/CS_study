import sys


N = int(sys.stdin.readline())

dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N)]

for i in range(10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N-1]) % 10007)
