import sys

n, p = map(int, sys.stdin.readline().split())

stacks = dict()
cnt = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a not in stacks:
        stacks[a] = [b]
        cnt += 1
    else:
        if len(stacks[a]) == 0:
            stacks[a].append(b)
            cnt += 1
        else:
            while len(stacks[a]) != 0 and stacks[a][-1] > b:
                stacks[a].pop()
                cnt += 1
            if len(stacks[a]) != 0 and stacks[a][-1] == b:
                pass
            else:
                stacks[a].append(b)
                cnt += 1
print(cnt)