import sys


def bfs():
    queue = [0]
    infested = []
    while queue:
        row = queue.pop(0)
        for i in range(N):
            if com[row][i] == 1 and i not in infested:
                infested.append(i)
                queue.append(i)
    return print(len(infested)-1)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

com = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    com[a-1][b-1] = 1
    com[b-1][a-1] = 1
bfs()
