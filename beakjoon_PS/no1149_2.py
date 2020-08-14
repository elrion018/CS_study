# 빨 0 초 1 파 2
# S 비용 배열
# D[i][j] = i번째 집을 j번째 색으로 칠했을 때 지금까지 집을 칠하는데 소비해온 비용
# D[i][j] =
# D[i][0] = min(D[i-1][1],D[i-1][2])  + S[i][0]

# 답 min(D[i][0], D[i][1], D[i][2])
import sys
S = []


N = int(sys.stdin.readline())
for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

D = [(S[0][0], S[0][1], S[0][2])]  # D[0][0], D[0][1], D[0][2] 추가

for i in range(1, N):
    temp1 = min(D[i-1][1], D[i-1][2]) + S[i][0]
    temp2 = min(D[i-1][0], D[i-1][2]) + S[i][1]
    temp3 = min(D[i-1][0], D[i-1][1]) + S[i][2]
    D.append((temp1, temp2, temp3))
print(min(D[N-1][0], D[N-1][1], D[N-1][2]))
