import sys

def dfs(vertex, target, adj, visited, ans):
  visited[vertex] = True
  for sub_vertex in adj[vertex]:
    if not visited[sub_vertex]:
      ans = dfs(sub_vertex, target, adj, visited, ans)

    elif visited[sub_vertex] and sub_vertex == target:
      ans.append(sub_vertex)

  return ans



n = int(sys.stdin.readline())

adj = [[] for _ in range(n+1)]


for i in range(1, n+1):
  adj[i].append(int(sys.stdin.readline()))

# print(adj)

ans = []

for i in range(1,n+1):
  visited = [False] * (n+1)
  ans = dfs(i, i, adj, visited, ans)

print(len(ans))

for i in ans:
  print(i)