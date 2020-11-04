import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    k = 2

    while True:
        temp = (2**(k)-1)
        x = n / temp
        if x == int(x):
            print(int(x))
            break
        k += 1
