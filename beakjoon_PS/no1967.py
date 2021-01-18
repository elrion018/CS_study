import sys
sys.setrecursionlimit(10**6)


def dfs(parent, sumVal):
    global maxVal, maxNode
    judge = True
    for node, weight in adj[parent]:  # dfs 메인로직
        if visited[node] == False:
            visited[node] = True
            dfs(node, sumVal + weight)
            visited[node] = False
            judge = False

    if judge:  # 종료 조건
        if sumVal > maxVal:
            maxVal = sumVal
            maxNode = parent
        return


n = int(sys.stdin.readline())

adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(n-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    adj[parent].append([child, weight])
    adj[child].append([parent, weight])

maxVal = -sys.maxsize
maxNode = None
visited[1] = True
dfs(1, 0)

temp = maxNode
maxVal = -sys.maxsize
maxNode = None

visited = [False] * (n+1)
visited[temp] = True
dfs(temp, 0)
print(maxVal)
