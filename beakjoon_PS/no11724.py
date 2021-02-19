import sys
import collections


def bfs(st):
    global ans
    q = collections.deque()
    q.append(st)
    check[st] = 1
    while q:
        x = q.popleft()
        for ax in adj[x]:
            if check[ax] == 0:
                check[ax] = 1
                q.append(ax)
    ans += 1
    return


N, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]
check = [0] * (N+1)
ans = 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N+1):
    if check[i] == 0:
        bfs(i)
print(ans)
