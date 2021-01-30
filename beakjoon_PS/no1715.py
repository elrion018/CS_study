import sys
import heapq

N = int(sys.stdin.readline())

q = []

for _ in range(N):
    heapq.heappush(q, int(sys.stdin.readline()))
res = 0
while len(q) > 1:
    temp1 = heapq.heappop(q)
    temp2 = heapq.heappop(q)
    heapq.heappush(q, temp1 + temp2)
    res += (temp1 + temp2)
print(res)
