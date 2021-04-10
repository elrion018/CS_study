import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n)

for i in range(n):
  dp[i] = arr[i]

  for j in range(i-1, -1, -1):
    if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
      dp[i] = dp[j] + arr[i]

print(max(dp))