import sys


def prime_list(n):
    sieve = [True] * n

    m = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    sieve[0] = False
    sieve[1] = False
    return sieve


table = prime_list(10001)


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    ans = None
    for i in range(2, n):
        if table[i] == True:
            temp = n - i
            if table[temp] == True:
                if ans is None:
                    ans = [i, temp]
                else:
                    if abs(ans[0]-ans[1]) > abs(i-temp):
                        ans = [i, temp]
    ans = sorted(ans)
    print(" ".join(list(map(str, ans))))
