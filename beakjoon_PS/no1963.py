import sys
import math
import collections


def get_prime():
    prime = [True]*(10001)
    for i in range(2, int(math.sqrt(10001))+1):
        if prime[i]:
            for j in range(i+i, 10001, i):
                prime[j] = False
    return prime


def bfs(a, b):
    q = collections.deque()
    visited = [False]*(10001)
    q.append([a, 0])
    visited[a] = True

    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt
        x = list(str(x))
        for i in range(4):
            for j in range(10):
                ax = x[:]
                ax[i] = str(j)
                ax = int("".join(ax))
                if ax >= 1000 and visited[ax] == False and prime[ax]:
                    visited[ax] = True
                    q.append([ax, cnt+1])

    return "Impossible"


prime = get_prime()
T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))
