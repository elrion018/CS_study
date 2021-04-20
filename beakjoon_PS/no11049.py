import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] *(n) for _ in range(n)]

for i in range(1, n): # 대각선 선택
  for j in range(n - i): # 대각선에서 열 선택

    if i == 1:
      dp[j][i+j] = arr[j][0] * arr[j][1] * arr[i+j][1]

    else:
      dp[j][i+j] = sys.maxsize

      for k in range(j, i+j):
        dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k+1][i+j] + arr[j][0] * arr[k][1] * arr[i+j][1])

print(dp[0][n-1])