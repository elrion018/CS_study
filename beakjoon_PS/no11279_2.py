import sys
import heapq

q = []

n = int(sys.stdin.readline())

for _ in range(n):
  num = int(sys.stdin.readline())

  if num == 0:
    if len(q) == 0:
      print(0)
    else:
      result = heapq.heappop(q)
      print(abs(result))

  else:
    heapq.heappush(q, -num)
