import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [sys.maxsize]*(N)
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if j + arr[j] >= i:
            dp[i] = min(dp[i], dp[j] + 1)
if dp[N-1] != sys.maxsize:
    print(dp[N-1])
else:
    print(-1)
