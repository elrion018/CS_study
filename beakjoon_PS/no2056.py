import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)

for i in range(1, n+1):
  arr = list(map(int, sys.stdin.readline().split()))

  t = arr.pop(0)
  _ = arr.pop(0)

  for x in arr:
    dp[i] = max(dp[i], dp[x])

  dp[i] += t

print(max(dp))