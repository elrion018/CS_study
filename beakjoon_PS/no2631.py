import sys
N = int(sys.stdin.readline())

arr = [0]

dp = [1] * (N+1)

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

for i in range(2, N+1):
    for j in range(1, i):
        if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(N - max(dp))
