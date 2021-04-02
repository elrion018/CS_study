import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  dp = [[0]*(n) for _ in range(2)]

  arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

  if n == 1:
    print(max(arr[0][0], arr[1][0]))

  elif n == 2:
    print(max(arr[1][0] + arr[0][1] , arr[0][0] + arr[1][1]))
  
  else:
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]

    for j in range(2,n):
      dp[0][j] = max(dp[1][j-1], dp[0][j-2], dp[1][j-2]) + arr[0][j]
      dp[1][j] = max(dp[0][j-1], dp[0][j-2], dp[1][j-2]) + arr[1][j]

    print(max(max(dp[0]), max(dp[1])))




