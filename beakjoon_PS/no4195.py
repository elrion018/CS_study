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
        return node1

    parent[node1] = node2
    cnt[node2] += cnt[node1]


t = int(sys.stdin.readline())


for _ in range(t):
    cnt = dict()
    parent = dict()
    F = int(sys.stdin.readline())
    for _ in range(F):
        temp = sys.stdin.readline().split()
        if temp[0] not in cnt:
            cnt[temp[0]] = 1
            parent[temp[0]] = temp[0]
        if temp[1] not in cnt:
            cnt[temp[1]] = 1
            parent[temp[1]] = temp[1]

        merge(temp[0], temp[1])
        print(cnt[find(temp[0])])
