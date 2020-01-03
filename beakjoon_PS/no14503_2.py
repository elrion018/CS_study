import sys
sys.setrecursionlimit(1000000)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def cal():
    result = 0
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 2:
                result += 1
    print(result)
    return result


def run(r, c, d, count):
    return clean(r, c, d, count)


def rotate(d):
    if d == 0:
        return 3

    d = d - 1
    return d


def search(r, c, d, count):

    ad = rotate(d)
    ar = r + dr[ad]
    ac = c + dc[ad]
    ar2 = r - dr[d]
    ac2 = c - dc[d]

    #
    if count == 4 and _map[ar2][ac2] == 1:
        return cal()

    if count == 4:
        return search(ar2, ac2, d, 0)
    if _map[ar][ac] == 0:
        return clean(ar, ac, ad, 0)
    if _map[ar][ac] == 1 or _map[ar][ac] == 2:
        return search(r, c, ad, count + 1)


def clean(r, c, d, count):
    _map[r][c] = 2
    search(r, c, d, count)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]

run(r, c, d, 0)
