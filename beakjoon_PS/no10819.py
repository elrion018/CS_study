import sys


def bt(table, cnt, res):
    global maxVal
    if cnt == N:
        ans = 0
        for i in range(1, N):
            ans += abs(res[i] - res[i-1])

        maxVal = max(maxVal, ans)
        return

    for i in range(1, len(nums)):
        if table[i] == False:
            table[i] = True
            res.append(nums[i])
            bt(table, cnt+1, res)
            table[i] = False
            res.pop()


N = int(sys.stdin.readline())

nums = [0] + list(map(int, sys.stdin.readline().split()))
table = [False] * (N+1)
maxVal = -sys.maxsize
bt(table, 0, [])
print(maxVal)
