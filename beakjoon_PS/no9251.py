import sys

A = list(sys.stdin.readline().rstrip('\n'))
B = list(sys.stdin.readline().rstrip('\n'))

D = [[0] * (len(B)+1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            D[i][j] = D[i-1][j-1] + 1
        else:
            D[i][j] = max(D[i][j-1], D[i-1][j])
print(D[-1][-1])
