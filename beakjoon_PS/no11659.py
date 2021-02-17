import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
_sum = [0]*(N+1)
_sum[1] = arr[1]
for i in range(2, len(arr)):
    _sum[i] = _sum[i-1] + arr[i]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    res = _sum[b] - _sum[a-1]
    print(res)
