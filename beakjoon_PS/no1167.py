import sys

sys.setrecursionlimit(10**6)

def dfs(now_node, sum_value, visited):
  global max_node, max_value

  if visited[now_node] != None:
    return

  visited[now_node] = sum_value

  for next_node, next_weight in adj[now_node]:
    dfs(next_node, sum_value + next_weight, visited)

  if max_value < visited[now_node]:
    max_value = visited[now_node]
    max_node = now_node

v = int(sys.stdin.readline())
adj = [[] for _ in range(v+1)]

for i in range(1, v+1):
  edges = list(map(int, sys.stdin.readline().split()))
  edges.pop()

  for j in range(1, len(edges), 2):
    node, weight = edges[j], edges[j+1]
    adj[edges[0]].append([node, weight])
  
visited = [None] * (v+1)
max_node = None
max_value = -sys.maxsize

dfs(1, 0, visited)

visited = [None] * (v+1)
temp = max_node
max_node = None
max_value = -sys.maxsize

dfs(temp, 0, visited)

print(max_value)