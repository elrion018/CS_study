import sys

def bs(arr, dough, end):
  
  start = 0
  idx = 0

  while start <= end:
    mid = (start + end) // 2

    if arr[mid] >= dough:
      start = mid + 1
      if idx == None:
        idx = mid
      else:
        if idx < mid:
          idx = mid
    

    else:
      end = mid - 1
      
  return idx


d, n = map(int, sys.stdin.readline().split())

arr1 = list(map(int, sys.stdin.readline().split())) # 오븐의 지름
temp = arr1[0]
for i in range(1,len(arr1)):
  if temp <= arr1[i]:
    arr1[i] = temp
  else:
    temp = arr1[i]

arr2 = list(map(int, sys.stdin.readline().split())) # 반죽의 지름
ans = None

end = d - 1
for i in range(n):
  idx = bs(arr1, arr2[i], end)
  ans = idx
  end = idx-1

if ans == 0:
  print(0)
else:
  print(ans+1)