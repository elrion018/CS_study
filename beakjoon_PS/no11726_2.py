

# D[i] = i번째 타일을 채우는 경우의 수
# D[i][j] = i번째 타일을 j유형 타일로 채우는 경우의 수

#D[i][1] = D[i-1][1] + D[i-1][2]
#D[i][2] = D[i-2][1] + D[i-2][2]
# D[i][1] + D[i][2]
import sys
N = int(sys.stdin.readline())
D = [(1, 0), (1, 1), (2, 1)]
if N >= 3:
    for i in range(3, N):
        temp1 = D[i-1][0] + D[i-1][1]
        temp2 = D[i-2][0] + D[i-2][1]
        D.append((temp1, temp2))
print((D[N-1][0] + D[N-1][1]) % 10007)
