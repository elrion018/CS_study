# D[i] 가치의 합이 i일때 사용한 동전의 경우의 수
# D[i] = D[i-1] + i-k에 들어갈 수 있는 동전들의 수

import sys
n, k = map(int, sys.stdin.readline().split())
coins = [0]
D = [[0]*(k+1) for _ in range(n+1)]


for i in range(n):
    coins.append(int(sys.stdin.readline()))
for i in range(1, n+1):
    for j in range(1, k+1):
        if j % coins[i] == 0:
            D[i][j] += 1
for i in range(2, n+1):
    for j in range(1, k+1):
        if j < coins[i]:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = D[i-1][j] + D[i][j-coins[i]]


print(D)
