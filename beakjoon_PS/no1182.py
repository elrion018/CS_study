import sys


def solve(idx, acc):
    global ans
    if idx >= N:
        if acc == S:
            ans += 1
        return
    solve(idx+1, acc + arr[idx])
    solve(idx+1, acc)


N, S = map(int, sys.stdin.readline().split())

ans = 0
arr = list(map(int, sys.stdin.readline().split()))
chk = [0]*N
solve(0, 0)
if S == 0:
    ans -= 1
print(ans)
