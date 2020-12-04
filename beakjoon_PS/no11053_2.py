# D[i] = i번째 항을 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [1 for i in range(N)]
for i in range(1, N):
    for j in range(i, -1, -1):
        if A[i] > A[j] and D[j] >= D[i]:
            D[i] = D[j] + 1
print(max(D))
