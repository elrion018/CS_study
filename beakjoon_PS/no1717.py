import sys


def init():  # 초기화 함수
    for i in range(n+1):
        parent[i] = i  # 처음 노드의 부모노드는 자기자신
        level[i] = 1  # 처음엔 노드 i가 속한 트리의 레벨은 1이다
    return


def find(node):  # node의 루트노드를 찾는 함수
    if node == parent[node]:  # node의 부모노드가 자기 자신이라면
        return node

    parent[node] = find(parent[node])  # 아니라면 루트노드를 계속 찾는다.
    return parent[node]


def merge(node1, node2):  # node1, node2가 있는 각각의 트리를 합치는 함수
    node1 = find(node1)  # 각각의 루트 노드를 찾아준다.
    node2 = find(node2)

    if node1 == node2:  # 루트 노드가 같다면 같은 트리
        return
    if level[node1] > level[node2]:  # node1이 더 작은 트리가 되도록한다
        node1, node2 = node2, node1

    parent[node1] = node2  # node1 루트노드의 부모가 node2이 되도록

    # node1와 node2의 level이 같을 때 node2의 레벨을 늘려준다.
    if level[node1] == level[node2]:
        level[node2] += 1


n, m = map(int, sys.stdin.readline().split())

parent = [0]*(n+1)  # 노드 i의 부모노드를 저장
level = [0]*(n+1)  # 노드 i가 속한 트리의 레벨

init()
for i in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        merge(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
print(parent)
