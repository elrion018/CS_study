import sys


N, S, M = map(int, sys.stdin.readline().split())

arr = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[False]*(M+1) for _ in range(N+1)]

dp[0][S] = True

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j] == False:
            continue
        if j - arr[i] >= 0:
            dp[i][j-arr[i]] = True

        if j + arr[i] <= M:
            dp[i][j+arr[i]] = True
ans = -1
for i in range(M+1):
    if dp[N][i]:
        ans = i
print(ans)
