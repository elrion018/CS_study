import sys

N, M = map(int, sys.stdin.readline().split())

memo = [0] + list(map(int, sys.stdin.readline().split()))
costs = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0]*(10001) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 10001):
        dp[i][j] = dp[i-1][j]
        if j - costs[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-costs[i]] + memo[i])
ans = sys.maxsize
for i in range(len(dp[N])):
    if dp[N][i] >= M:
        ans = min(ans, i)
print(ans)
