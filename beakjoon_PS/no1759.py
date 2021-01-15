import sys


def bt(cnt):
    if cnt == L:
        mo = 0
        ja = 0
        for i in range(len(res)):
            if res[i] in ['a', 'e', 'i', 'o', 'u']:
                mo += 1
            else:
                ja += 1
        if mo >= 1 and ja >= 2:
            for i in range(len(res)):
                if i == len(res) - 1:
                    print(res[i])
                else:
                    print(res[i], end='')
            return
        else:
            return

    for i in range(C):
        if len(res) == 0:
            res.append(S[i])
            bt(cnt+1)
            res.pop()
        else:
            if ord(res[-1]) < ord(S[i]):
                res.append(S[i])
                bt(cnt+1)
                res.pop()

    return


L, C = map(int, sys.stdin.readline().split())

S = list(sys.stdin.readline().split())
S = sorted(S)
res = []

bt(0)
