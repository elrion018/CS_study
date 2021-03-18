import sys, collections

def bfs(n, st, adj, res1):
  visited = [0] * (n+1)
  q = collections.deque()
  q.append(st)

  while q:
    v = q.popleft()
    if not visited[v]:
      visited[v] = 1
      res1.append(v)

    for sv in adj[v]:
      if not visited[sv]:
        q.append(sv)

  return res1


def dfs(n, st, adj, res2):
  visited = [0] * (n+1)
  stack = []
  stack.append(st)

  while stack:
    v = stack.pop()
    if visited[v] == 0:
      visited[v] = 1
      res2.append(v)

    for sv in sorted(adj[v], reverse=True):
      if not visited[sv]:
        stack.append(sv)
        
  return res2

n, m, v = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
  s, e = map(int, sys.stdin.readline().split())

  adj[s].append(e)
  adj[e].append(s)

for i in range(1, len(adj)):
  adj[i] = sorted(adj[i])

print(" ".join(map(str,dfs(n, v, adj, []))))
print(" ".join(map(str,bfs(n, v, adj, []))))