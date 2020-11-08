import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split(" ")))
    b = list(map(int, sys.stdin.readline().split(" ")))
    for _ in range(k):
        a_min = min(a)
        b_max = max(b)
        if a_min >= b_max:
            break
        a_min_i = a.index(a_min)
        b_max_i = b.index(b_max)
        a[a_min_i] = b_max
        b[b_max_i] = a_min
    print(sum(a))
