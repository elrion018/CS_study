import sys

def get_adj_list(n,m):
	adj = [[] for _ in range(n+1)]

	for _ in range(m):
		a, b = map(int,sys.stdin.readline().split())
		adj[a].append(b)
		adj[b].append(a)

	return adj

def dfs(adj, visited):
	visited[1], stack, cnt = True, [1], 0

	while stack:
		vertex = stack.pop()

		for i in adj[vertex]:
			if visited[i] == False:
				visited[i] = True
				cnt += 1
				stack.append(i)
	
	return cnt

def solution(n,m):
	adj = get_adj_list(n,m)
	visited = [False] *(n+1)
	
	return dfs(adj, visited)

t = int(sys.stdin.readline())

for _ in range(t):
	n, m = map(int,sys.stdin.readline().split())
	print(solution(n,m))