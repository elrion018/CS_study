# D[i] = B의 i번째 위치를 마지막으로 했을때 전깃줄의 최대 갯수

import sys

N = int(sys.stdin.readline())
lines = []
for _ in range(N):
    lines.append(list(map(int, sys.stdin.readline().split())))
lines = sorted(lines, key=lambda element: element[1])
D = [1 for _ in range(501)]

for i in range(1, N):
    D[i] = 1
    for j in range(i, -1, -1):
        if lines[j][0] < lines[i][0] and D[j] >= D[i]:
            D[i] = D[j] + 1
print(N-max(D))
