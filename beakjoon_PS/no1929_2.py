import sys, math

def sieve(n):
  numbers = [True] * (n+1)
  
  for i in range(2,int(math.sqrt(n+1))+1):
    if numbers[i] == True:
      for j in range(i+i, n+1,i):
        numbers[j] = False

  return [i for i in range(2, n+1) if numbers[i] == True]

m, n = map(int, sys.stdin.readline().split())

for number in sieve(n):
  if number >= m:
    print(number)

