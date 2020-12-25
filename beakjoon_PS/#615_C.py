import sys
import math
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    a = None
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            a = i
            break
    if a == None:
        print("NO")
        continue
    b = None
    for j in range(2, int(math.sqrt(n))):
        if (n//i) % j == 0 and j != a:
            b = j
            break
    if b == None:
        print("NO")
        continue

    if n // (a*b) != a and n // (a*b) != b and n // (a*b) != 1:
        c = n // (a*b)
    else:
        print("NO")
        continue

    print("YES")
    print(a, b, c)
