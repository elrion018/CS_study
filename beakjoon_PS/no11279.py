import sys
import heapq


def insert(x):
    heapq.heappush(q, [-x, x])
    return


def pop():
    if len(q) == 0:
        return 0
    else:
        return heapq.heappop(q)[1]


q = []
N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(pop())
    else:
        insert(x)
