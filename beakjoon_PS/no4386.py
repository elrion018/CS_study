import sys
import math


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
        level[node1] += 1


n = int(sys.stdin.readline())

stars = []

for _ in range(n):
    stars.append(list(map(float, sys.stdin.readline().split())))

line = []

for i in range(n):
    for j in range(i+1, n):
        dist = math.sqrt((abs(stars[i][0] - stars[j][0]))
                         ** 2+(abs(stars[i][1] - stars[j][1])**2))
        line.append([i+1, j+1, dist])

line = sorted(line, key=lambda ele: ele[2])

parent = [i for i in range(n+1)]
level = [0] * (n+1)
cost = 0
for node1, node2, c in line:
    merge(node1, node2, c)
print("%.2f" % cost)
