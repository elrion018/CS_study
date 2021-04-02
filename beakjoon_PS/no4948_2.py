import sys, math

def get_prime_numbers(n):
  sieve = [True] * (2*n + 1)

  for i in range(2, int(math.sqrt(2*n)+1)):
    if sieve[i] == True:
      for j in range(i+i, 2*n + 1, i):
        sieve[j] = False

  return [i for i in range(n+1, 2*n + 1) if sieve[i] == True]


while True:
  n = int(sys.stdin.readline())

  if n == 0:
    break

  print(len(get_prime_numbers(n)))

