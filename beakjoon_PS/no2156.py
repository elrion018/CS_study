# D[i]i번째 포도주까지 마신 포도주 양의 최댓값
# W 와인 배열
# D[i] = max(D[i-1], D[i-2] + W[i], D[i-3] + W[i] + W[i-1]  )
import sys
import collections

N = int(sys.stdin.readline())
W = collections.deque()
for _ in range(N):
    W.append(int(sys.stdin.readline()))

D = collections.deque()
if N == 1:
    D.append(W[0])  # D[0]
if N == 2:
    D.append(W[0])  # D[0]
    D.append(W[0] + W[1])  # D[1]
if N >= 3:
    D.append(W[0])  # D[0]
    D.append(W[0] + W[1])  # D[1]
    D.append(max(W[0]+W[1], W[0]+W[2], W[1]+W[2]))  # D[2]

    for i in range(3, N):
        temp = max(D[i-1], D[i-2] + W[i], D[i-3] + W[i] + W[i-1])
        D.append(temp)
print(max(D))
