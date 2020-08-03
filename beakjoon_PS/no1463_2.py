import sys
# D[i] = i를 1로 만들기 위해 필요한 연산 사용 횟수의 최솟값.

N = int(sys.stdin.readline())

D = [0] * (N+1)
D[1] = 0

for k in range(2, N+1):
    if k % 2 == 0 and k % 3 == 0:
        D[k] = min(D[k-1]+1, D[k//2]+1, D[k//3] + 1)

    elif k % 2 != 0 and k % 3 != 0:
        D[k] = D[k-1]+1

    elif k % 2 == 0:
        D[k] = min(D[k-1]+1, D[k//2]+1)
    elif k % 3 == 0:
        D[k] = min(D[k-1]+1, D[k//3]+1)

print(D[N])
