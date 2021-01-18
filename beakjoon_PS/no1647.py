import sys


def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def merge(node1, node2, c):
    global cost, maxVal
    node1 = find(node1)
    node2 = find(node2)

    if node1 == node2:
        return
    if level[node1] > level[node2]:
        node1, node2 = node2, node1
    parent[node1] = node2
    cost += c
    maxVal = max(maxVal, c)
    if level[node1] == level[node2]:
        level[node2] += 1


N, M = map(int, sys.stdin.readline().split())
roads = []
for _ in range(M):
    roads.append(list(map(int, sys.stdin.readline().split())))

roads = sorted(roads, key=lambda ele: ele[2])

parent = [i for i in range(N+1)]
level = [0] * (N+1)

maxVal = -sys.maxsize
cost = 0

for node1, node2, c in roads:
    merge(node1, node2, c)
print(cost - maxVal)
