import sys


def dfs(st):
    stack = [st]

    while stack:
        vec = stack.pop()
        for i in adj[vec]:
            if table[i] == 0:
                table[i] = vec
                stack.append(i)


N = int(sys.stdin.readline())

table = [0] * (N+1)
table[1] = 1
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1)

for i in range(2, len(table)):
    print(table[i])
