import sys


def bt(table, res):

    for i in range(1, N+1):
        if table[i] == False:
            table[i] = True
            res.append(i)
            bt(table, res)
            table[i] = False
            res.pop()
    if len(res) == N:
        print(" ".join(map(str, res)))

    return


N = int(sys.stdin.readline())

res = []
table = [False] * (N+1)
bt(table, res)
