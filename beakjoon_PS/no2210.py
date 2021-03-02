import sys


def dfs(sty, stx, cnt, digit):
    global nums
    if cnt == 5:
        if digit not in nums:
            nums.append(digit)
        return
    for i in range(4):
        ay = sty + dy[i]
        ax = stx + dx[i]
        if ay >= 0 and ay < 5 and ax >= 0 and ax < 5:
            temp = digit + arr[ay][ax]
            dfs(ay, ax, cnt+1, temp)


arr = [sys.stdin.readline().split() for _ in range(5)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
nums = []

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, arr[i][j])

print(len(nums))
