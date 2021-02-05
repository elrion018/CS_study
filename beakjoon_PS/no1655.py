import sys
import heapq
N = int(sys.stdin.readline())

minq = []
maxq = []
for _ in range(N):
    temp = int(sys.stdin.readline())
    if len(maxq) == 0:
        heapq.heappush(maxq, [-temp, temp])
        print(maxq[0][1])
        continue
    if len(maxq) == len(minq):
        heapq.heappush(maxq, [-temp, temp])
    else:
        heapq.heappush(minq, temp)

    if len(minq) != 0:
        maxtop = heapq.heappop(maxq)[1]
        mintop = heapq.heappop(minq)
        if maxtop > mintop:
            heapq.heappush(maxq, [-mintop, mintop])
            heapq.heappush(minq, maxtop)
            print(maxq[0][1])
        else:
            heapq.heappush(maxq, [-maxtop, maxtop])
            heapq.heappush(minq, mintop)
            print(maxq[0][1])
