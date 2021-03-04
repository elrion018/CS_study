import sys

T = int(sys.stdin.readline())

for _ in range(T):
    dp = [[0, 0, 0] for _ in range(1000001)]
    n = int(sys.stdin.readline())
    dp[1][0] = 1
    dp[2][0] = 1
    dp[2][1] = 1
    dp[3][0] = 2
    dp[3][1] = 1
    dp[3][2] = 1
    if n < 4:
        print(sum(dp[n]) % 1000000009)
    else:
        for i in range(4, n+1):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 1000000009
            dp[i][1] = (dp[i-2][0] + dp[i-2][1] + dp[i-2][2]) % 1000000009
            dp[i][2] = (dp[i-3][0] + dp[i-3][1] + dp[i-3][2]) % 1000000009
        print(sum(dp[n]) % 1000000009)
