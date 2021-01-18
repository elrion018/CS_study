import sys


def find(node):

    if node == parent[node]:
        return node

    parent[node] = find(parent[node])
    return parent[node]


def merge(node1, node2, c):
    global cost
    node1 = find(node1)
    node2 = find(node2)

    if node1 == node2:
        return
    if level[node1] > level[node2]:
        node1, node2 = node2, node1

    parent[node1] = node2
    cost += c
    if level[node1] == level[node2]:
        level[node2] += 1


N, M = map(int, sys.stdin.readline().split())
arr = []

parent = [i for i in range(N+1)]
level = [1] * (N+1)

for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)

arr = sorted(arr, key=lambda ele: ele[2])

cost = 0

for node1, node2, c in arr:
    merge(node1, node2, c)
print(cost)
