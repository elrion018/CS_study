import sys

n = int(sys.stdin.readline())

arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0,0] for _ in range(n+1)]

dp[1] = [arr[1], arr[1]]


for i in range(2, n+1):
  dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
  dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0])

# print(dp)

max_val = -sys.maxsize


for i in range(1,n+1):
  max_val = max(max_val, max(dp[i]))

print(max_val)
