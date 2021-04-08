import sys, itertools

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, len(arr)+1):
  cases = itertools.combinations(arr, i)

  for case in cases:
    sum_of_case = sum(case)

    if sum_of_case == s:
      count += 1

print(count)

