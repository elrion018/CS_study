import sys


def prime_list(N):
    table = [True] * (N+1)

    for i in range(2, int(N**0.5)+1):
        if table[i] == True:
            for j in range(i+i, N+1, i):
                table[j] = False

    return [i for i in range(2, N+1) if table[i] == True]


N = int(sys.stdin.readline())

table = prime_list(N)


while N != 1:
    for i in range(len(table)):
        if N % table[i] == 0:
            N = N // table[i]
            print(table[i])
            break
