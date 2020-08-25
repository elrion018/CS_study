# D[i][j] i번째 층 j번쨰 수에서 시작해 맨밑층까지 내려갔을 때 이제까지 선택된 수의 합 중 최댓값
# D[i][j] = max(D[i-1][j], D[i-1][j+1]) + S[i][j]


import sys
import collections
N = int(sys.stdin.readline())
S = collections.deque()
for _ in range(N):
    S.appendleft(list(map(int, sys.stdin.readline().split())))

D = []
temp = []
for i in range(N):
    temp.append(S[0][i])
D.append(temp)

for i in range(1, N):
    temp = []
    for j in range(N-i):
        temp.append(max(D[i-1][j], D[i-1][j+1]) + S[i][j])
    D.append(temp)
print(D[N-1][0])
