# D[i][j] i개의 자리수일때 숫자 j가 맨 뒤에 올 수 있는 경우의 수
# j = 0 D[i][j] = D[i-1][1]
# j = 9 D[i][j] = D[i-1][8]
# j = 1 ~ 8 D[i][j] = D[i-1][j-1] + D[i-1][j+1]

import sys
N = int(sys.stdin.readline())
D = [[0]*10 for j in range(101)]
for i in range(1, 10):
    D[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            D[i][j] = D[i-1][1]
        elif j == 9:
            D[i][j] = D[i-1][8]
        else:
            D[i][j] = D[i-1][j-1] + D[i-1][j+1]
print(sum(D[N]) % 1000000000)
