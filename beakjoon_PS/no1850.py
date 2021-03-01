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
gcd = gcd(a, b)

print('1'*gcd)
