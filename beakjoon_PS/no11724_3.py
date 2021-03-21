import sys

sys.setrecursionlimit(10**6)

def dfs(vertex, adj, visited):
  if visited[vertex] == 0:
    visited[vertex] = 1

    for next_vertex in adj[vertex]:
      if visited[next_vertex] == 0:
        visited = dfs(next_vertex, adj, visited)
    
    return visited

  return visited

n, m = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
  u, v = map(int, sys.stdin.readline().split())

  adj[u].append(v)
  adj[v].append(u)

for vertex in range(1, n+1):
  if visited[vertex] == 0:
    visited = dfs(vertex, adj, visited)
    cnt += 1

print(cnt)