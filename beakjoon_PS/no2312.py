import sys
import math

def getPrimeNum():
    sieve = [True]*(100001)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(100001)+1)):
        if sieve[i] == True:
            for j in range(i+i, 100001, i):
                sieve[j] = False
    return [i for i in range(2,100001) if sieve[i] == True]

primeNum = getPrimeNum()

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    table = [0] * (100001)

    while n != 1:
        for i in range(len(primeNum)):
            if n % primeNum[i] == 0:
                n = n//primeNum[i]
                table[primeNum[i]] += 1
                break
    for i in range(2,len(table)):
        if table[i] != 0:
            print(i, table[i])