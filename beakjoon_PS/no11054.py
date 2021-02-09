import sys

N = int(sys.stdin.readline())

arr = [0] + list(map(int, sys.stdin.readline().split()))

dp1 = [0] * (N+1)
dp2 = [0] * (N+1)
maxVal = -sys.maxsize
for i in range(1, N+1):
    dp1[i] = 1
    for j in range(1, i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
# print(dp1)

arr.reverse()
arr.pop()
arr = [0] + arr

for i in range(1, N+1):
    dp2[i] = 1
    for j in range(1, i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
# print(dp2)

for i in range(1, i+1):
    maxVal = max(maxVal, dp1[i] + dp2[N-i+1] - 1)
print(maxVal)
