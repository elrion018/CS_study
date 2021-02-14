import sys


def solve(N):
    if N == 1:
        return 'm'
    if N == 2 or N == 3:
        return 'o'
    i = 0

    while dp[i] < N:
        i += 1
        if N - dp[i-1] == 1:
            return 'm'
        if N - dp[i-1] <= i + 3:
            return 'o'
    return solve(N-dp[i-1]-(i+3))


N = int(sys.stdin.readline())

dp = [0]*(41)
dp[0] = 3

for i in range(1, 41):
    dp[i] = 2*dp[i-1] + i + 3
print(solve(N))
