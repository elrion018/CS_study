import sys

sys.setrecursionlimit(10**6)

def get(u, adj):
  global dp
  if dp[u] != None:
    return 0

  dp[u] = 1
  
  for vertex in adj[u]:
    dp[u] += get(vertex, adj)
  
  return dp[u]
  
    
n, r, q = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
dp = [None] * (n+1)
temp = []

for _ in range(n-1):
  u, v = map(int, sys.stdin.readline().split())

  adj[u].append(v)
  adj[v].append(u)

for _ in range(q):
  u = int(sys.stdin.readline())
  temp.append(u)

get(r, adj)

for u in temp:
  print(dp[u])