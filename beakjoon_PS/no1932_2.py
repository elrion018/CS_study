import sys

n = int(sys.stdin.readline())

num = []
for _ in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

dp = []

for i in range(1, n+1):
    dp.append([0]*i)

dp[0][0] = num[0][0]
if n == 1:
    print(dp[0][0])
else:
    for x in range(1, n):
        for y in range(x+1):
            if y == 0:
                dp[x][y] = dp[x-1][y] + num[x][y]
            elif y == x:
                dp[x][y] = dp[x-1][y-1] + num[x][y]
            else:
                dp[x][y] = max(dp[x-1][y-1] + num[x][y],
                               dp[x-1][y] + num[x][y])
    print(max(dp[n-1]))
