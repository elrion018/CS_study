
import sys

N = int(sys.stdin.readline())

stair = []
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

dp = [[0, 0] for _ in range(N)]
if N > 2:
    dp[0][0] = stair[0]
    dp[1][0] = stair[1]
    dp[1][1] = stair[0] + stair[1]
    dp[2][0] = stair[0] + stair[2]
    dp[2][1] = stair[1] + stair[2]

    for i in range(2, N):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stair[i]
        dp[i][1] = dp[i-1][0] + stair[i]

    print(max(dp[N-1][0], dp[N-1][1]))
elif N == 2:
    print(stair[0]+stair[1])
elif N == 1:
    print(stair[0])
