import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    prev = 0
    now = 0
    while True:
        now = (k // n) - prev
        k += now
        prev += now
        now = k // n
        if prev == now:
            print(k)
            break
