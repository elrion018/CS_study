import sys

n = [0] + int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * (n+1)

for i in range(2, n+1):
    for j in range(1, i):
        if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
