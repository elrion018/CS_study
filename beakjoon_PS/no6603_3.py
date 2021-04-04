import sys, itertools

while True:
  arr = list(map(int, sys.stdin.readline().split()))

  if arr[0] == 0:
    break

  k, arr = arr[0], arr[1:]
  ans = list(itertools.combinations(arr, 6))

  for i in range(len(ans)):
    print(" ".join(list(map(str,list(ans[i])))))
  print("")