import sys


def bt(c):

    for i in range(1, c//2 + 1):
        if res[-i:] == res[-2*i:-i]:
            return -1

    if c == N:
        print("".join(list(map(str, res))))
        return 0

    for i in range(1, 4):
        res.append(i)
        if bt(c+1) == 0:
            return 0
        res.pop()


N = int(sys.stdin.readline())
res = []
bt(0)
