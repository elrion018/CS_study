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


t = int(sys.stdin.readline())

for _ in range(t):
    N = int(sys.stdin.readline())
    enemy = [0]
    parent = [i for i in range(N+1)]
    level = [1 for _ in range(N+1)]

    for _ in range(N):
        enemy.append(list(map(int, sys.stdin.readline().split())))
    for i in range(1, N+1):
        st = enemy[i]
        for j in range(1, N+1):
            if i != j:
                if (st[2]+enemy[j][2]) ** 2 >= (enemy[j][0] - st[0])**2 + (enemy[j][1] - st[1])**2:
                    merge(i, j)

    for i in range(1, N+1):
        find(i)
    parent = sorted(parent)
    res = 1
    now = parent[1]
    for i in range(1, len(parent)):
        if parent[i] != now:
            res += 1
            now = parent[i]
    print(res)
