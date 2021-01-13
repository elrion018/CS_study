import sys


def find(node):

    if node == parent[node]:
        return node

    parent[node] = find(parent[node])
    return parent[node]


def merge(node1, node2):
    node1 = find(node1)
    node2 = find(node2)

    if node1 == node2:
        return

    if A[node1] >= A[node2]:
        parent[node1] = node2
    else:
        parent[node2] = node1


N, M, k = map(int, sys.stdin.readline().split())

A = [0] + list(map(int, sys.stdin.readline().split()))

re = []

parent = [i for i in range(N+1)]


for _ in range(M):
    re.append(list(map(int, sys.stdin.readline().split())))
for i in range(len(re)):
    merge(re[i][0], re[i][1])
for i in range(N+1):
    find(i)

parent = sorted(parent)
res = 0
now = parent[0]

for i in range(N+1):
    if now != parent[i]:
        res += A[parent[i]]
        now = parent[i]
if res <= k:
    print(res)
else:
    print("Oh no")
