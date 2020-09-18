import sys


T = int(sys.stdin.readline())
for _ in range(T):
    P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    N = int(sys.stdin.readline())
    for i in range(10, N):
        temp = P[i-1] + P[i-5]
        P.append(temp)
    print(P[N-1])
