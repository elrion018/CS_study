import sys

def bs(arr, target):
  start = 0
  end = len(arr)-1

  while start <= end:
    mid = (start + end) // 2

    if arr[mid] <= target:
      start = mid +1

    else:
      end = mid -1

  return end

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

ans = sys.maxsize

ans_index =[None, None]

for i in range(len(arr)):
  l = bs(arr, -arr[i])
  r = l +1

  if l == i:
    l -= 1

  if r == i:
    r += 1

  if l >= 0 and l <n and abs(arr[i] + arr[l]) < ans:
    ans = abs(arr[i] + arr[l])
    ans_index = [i, l]

  if r >= 0 and r < n and abs(arr[i] + arr[r]) <ans:
    ans = abs(arr[i] + arr[r])
    ans_index = [i, r]

ans_index.sort()

print(arr[ans_index[0]], arr[ans_index[1]])
