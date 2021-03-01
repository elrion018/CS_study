import sys


def gcd(a, b):
    if a < b:
        a, b = b, a

    while True:
        n = a % b
        if n == 0:
            return b
        else:
            a = b
            b = n


a, b = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())


c, m = (a*y + x*b), b*y

while True:
    div = gcd(c, m)
    if div == 1:
        break
    else:
        c = c // div
        m = m // div
print(c, m)
