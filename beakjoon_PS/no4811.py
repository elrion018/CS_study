import sys

dp = [[0] * 32 for _ in range(32)]

for i in range(31):
  dp[0][i] = 1

for i in range(1,31):
  for j in range(31):
    if j == 0:
      dp[i][j] = dp[i-1][1]
    else:
      # print(i,j)
      dp[i][j] = dp[i-1][j+1] + dp[i][j-1]

while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break

  print(dp[n-1][1])