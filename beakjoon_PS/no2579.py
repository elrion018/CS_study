# S 점수 배열
# D[i][j] = j개의 연속된 계단을 올라 i에 도착했을 때 얻을 수 있는 점수의 최댓값
# D[i][1]과 D[i][2]가 있을 수 있다.
#D[i][1] = max(D[i-2][1], D[i-2][2]) + S[i]
# D[i][2] = D[i-1][1] + S[i]
import sys
N = int(sys.stdin.readline())
S = []
for _ in range(N):
    S.append(int(sys.stdin.readline()))
D = []
if N == 1:
    D.append((S[0], 0))  # D[1][1], D[1][2]
if N == 2:
    D.append((S[0], 0))  # D[1][1], D[1][2]
    D.append((S[1], S[0]+S[1]))  # D[2][1], D[2][2]

if N >= 3:
    D.append((S[0], 0))  # D[1][1], D[1][2]
    D.append((S[1], S[0]+S[1]))  # D[2][1], D[2][2]
    for i in range(2, N):  # D[i][1], D[i][2] 추가 해야함.
        D.append((max(D[i-2][0], D[i-2][1]) + S[i], D[i-1][0] + S[i]))
print(max(D[N-1][0], D[N-1][1]))
