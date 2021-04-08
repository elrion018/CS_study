import sys

string = list(sys.stdin.readline().strip())
bridge = [list(sys.stdin.readline().strip()) for _ in range(2)]
dic = dict()

for i in range(len(string)):
  if string[i] in dic:
    dic[string[i]].append(i+1)

  else:
    dic[string[i]] = [i+1]
    
dp = [[[0]*(len(string) + 1) for _ in range(len(bridge[0]))] for _ in range(2)]

for i in range(2):
  for j in range(len(bridge[0])):
    if bridge[i][j] in dic:
      bridge[i][j] = dic[bridge[i][j]]

    else:
      bridge[i][j] = []

for i in range(2):
  for j in range(len(bridge[0])):
    if len(bridge[i][j]) != 0 and bridge[i][j][0] == 1:
      dp[i][j][1] = 1


for j in range(1, len(bridge[0])):
  for i in range(2):
    for k in range(len(dp[i][j])):
      dp[i][j][k] += dp[i][j-1][k]

    for k in bridge[i][j]:
      if i == 0:
        dp[0][j][k] = dp[0][j][k] + dp[1][j-1][k-1]

      elif i == 1:
        dp[1][j][k] = dp[1][j][k] + dp[0][j-1][k-1]

print(dp[0][-1][-1] + dp[1][-1][-1])