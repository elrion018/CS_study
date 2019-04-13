#############
#백준 1912번 문제 연속합
#D[i] : i번째 항을 마지막으로하는 수열의 합(연속합 )의 최댓값
#D[i] = max(0, D[i-1]) + A[i] 0을 기준으로 분기를 나눈다.
##########################

import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
D = []
D.append(A[0])
for i in range(1,N):
    D.append(0)
    D[i] = max(0,D[i-1]) + A[i]
print(max(D))