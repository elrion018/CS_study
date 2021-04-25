import sys
import itertools

n = int(sys.stdin.readline())
cases = list(itertools.permutations(list(map(int, sys.stdin.readline().split())), n))
max_value = -sys.maxsize

for case in cases:
  sum_value = 0
  for i in range(1,len(case)):
    sum_value += abs(case[i] - case[i-1])

  max_value = max(max_value, sum_value)

print(max_value)