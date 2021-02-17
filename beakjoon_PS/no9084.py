import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in arr:
        for j in range(coin, M+1):
            dp[j] += dp[j-coin]
    print(dp[M])
