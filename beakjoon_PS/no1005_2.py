import sys
sys.setrecursionlimit(10**6)

def get(req, w):
  if dp[w] != None:
    return dp[w]

  st = 0

  for i in req[w]:
    st = max(st, get(req, i))

  dp[w] = st + costs[w]

  return dp[w]


t = int(sys.stdin.readline())

for _ in range(t):
  n, k = map(int, sys.stdin.readline().split())
  costs = [0] + list(map(int, sys.stdin.readline().split()))
  req = [[] for _ in range(n+1)]
  dp = [None]*(n+1)
  
  for _ in range(k):
    x, y = map(int,sys.stdin.readline().split())    
    req[y].append(x)

  w = int(sys.stdin.readline())

  print(get(req, w))
