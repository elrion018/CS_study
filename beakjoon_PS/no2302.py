import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dp = [0] * (41)

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
ans = 1
tmp = 0
for _ in range(M):
    k = int(sys.stdin.readline())
    ans *= dp[k-tmp-1]
    tmp = k
ans *= dp[N-tmp]
print(ans)
