import sys
import heapq
N = int(sys.stdin.readline())

q = []
temp = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    heapq.heappush(q, temp[i])
for _ in range(N-1):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        heapq.heappush(q, temp[i])
    for _ in range(N):
        heapq.heappop(q)

print(q)
