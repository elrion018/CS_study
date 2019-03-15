M, N = map(int,input().split())
sieve = [True]*(N+1)
sieve[1] = False

sq = int(N**0.5)
for i in range(2, sq+1):
    if sieve[i] == True:
        for j in range(i+i, N+1, i):
            sieve[j] = False

for i in range(M,N+1):
    if sieve[i] == True:
        print(i)
