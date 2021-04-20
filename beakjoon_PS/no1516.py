import sys

sys.setrecursionlimit(10**6)

def get(last):
  if dp[last] != None:
    return dp[last]

  start = 0
  for prev in request[last]:
    start = max(start, get(prev))

  dp[last] = start + costs[last]

  return dp[last]

n = int(sys.stdin.readline())
request = [[] for _ in range(n+1)]
costs = [0] * (n+1)
dp = [None] * (n+1)

for i in range(1, n+1):
  temp = list(map(int, sys.stdin.readline().split()))

  temp.pop()
  costs[i] = temp[0]

  if len(temp) >=2:
    request[i] = temp[1:]

for last in range(1, n+1):
  print(get(last))