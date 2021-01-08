import sys


def init():
    for i in range(N+1):
        parent[i] = i
        level[i] = 1
    return


def find(node):
    if parent[node] == node:
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
M = int(sys.stdin.readline())

parent = [0] * (N+1)
level = [0] * (N+1)
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

plan = list(map(int, sys.stdin.readline().split()))

init()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            merge(i+1, j+1)

root = None
judge = True
for i in range(len(plan)):
    if root == None:
        root = find(plan[i])
    else:
        if root != find(plan[i]):
            judge = False
            break
if judge:
    print("YES")
else:
    print("NO")
