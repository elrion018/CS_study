# D[i] = i번째 정수를 마지막으로 하는 수열의 합 중 최댓값
# 정수배열 S
# D[i] =  max(0,D[i-1]) + S[i]
import sys
N = int(sys.stdin.readline())

S = list(map(int, sys.stdin.readline().split()))

D = [S[0]]  # D[0] 추가
for i in range(1, N):
    temp1 = max(0, D[i-1]) + S[i]
    D.append(temp1)
print(max(D))
