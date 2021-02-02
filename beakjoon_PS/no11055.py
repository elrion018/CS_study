import sys

N = int(sys.stdin.readline())

arr = [0] + list(map(int, sys.stdin.readline().split()))


dp = [0] * (N+1)

dp[1] = arr[1]

for i in range(2, N+1):
    dp[i] = arr[i]
    for j in range(1, i):
        if arr[i] > arr[j] and dp[j] + arr[i] > dp[i]:
            dp[i] = dp[j] + arr[i]

print(max(dp))
