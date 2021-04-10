import sys

def bt(arr, sum_value, idx, n, s):
  return_value = 0

  if idx == n:
    if sum_value == s:

      return 1
    
    return 0
  
  return_value += bt(arr, sum_value + arr[idx], idx+1, n, s)
  return_value += bt(arr, sum_value, idx+1, n, s)

  return return_value

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0

count += bt(arr, 0, 0, n, s)

if s == 0:
  count -= 1

print(count)