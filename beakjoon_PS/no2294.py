import sys

n, k = map(int, sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [sys.maxsize]*(10001)
dp[0] = 0
arr.sort()
for i in arr:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i] + 1)
if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
