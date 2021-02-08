import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    dp = [[0, 0, 0] for _ in range(n)]

    arr = [[] for _ in range(n)]
    temp1 = list(map(int, sys.stdin.readline().split()))
    for i in range(len(temp1)):
        arr[i].append(temp1[i])
    temp2 = list(map(int, sys.stdin.readline().split()))
    for i in range(len(temp2)):
        arr[i].append(temp2[i])
    dp[0][0] = 0
    dp[0][1] = arr[0][0]
    dp[0][2] = arr[0][1]
    maxVal = -sys.maxsize
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + arr[i][0]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + arr[i][1]
        maxVal = max(dp[i][0], dp[i][1], dp[i][2])
    print(maxVal)
