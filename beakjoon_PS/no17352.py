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

    if level[node1] > level[node2]:
        node1, node2 = node2, node1

    parent[node1] = node2

    if level[node1] == level[node2]:
        level[node2] += 1


N = int(sys.stdin.readline())

parent = [i for i in range(N+1)]
level = [1] * (N+1)
for _ in range(N-2):
    temp = list(map(int, sys.stdin.readline().split()))
    merge(temp[0], temp[1])
for i in range(1, N+1):
    find(i)
parent = list(set(parent))

for i in range(len(parent)):
    if parent[i] != 0:
        print(parent[i], end=' ')
