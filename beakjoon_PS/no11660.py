import sys


def solve(x1, y1, x2, y2):
    res = psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1]
    return res


N, M = map(int, sys.stdin.readline().split())

arr = []
psum = []
for _ in range(N+1):
    if _ == 0:
        arr.append([0]*(N+1))
    else:
        arr.append([0]+list(map(int, sys.stdin.readline().split())))
    psum.append([0]*(N+1))

for i in range(1, N+1):
    for j in range(1, N+1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1] - \
            psum[i-1][j-1] + arr[i][j]

# print(arr)
# print(psum)


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(solve(x1, y1, x2, y2))
