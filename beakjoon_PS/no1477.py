import sys

n, m, l = map(int, sys.stdin.readline().split())

arr = [0] + list(map(int, sys.stdin.readline().split())) + [l]
arr.sort()

# print(arr)
start = 0
end = l -1

ans = sys.maxsize

while start <= end:
  mid = (start + end) // 2
  new = 0
  for i in range(1,len(arr)):
    dist = abs(arr[i] - arr[i-1])
    new += dist // mid
    if dist % mid == 0:
        new -= 1

  
  
  if new > m: # 세워야할 편의점보다 더 많이 생김
    start = mid +1
    

  else: # 세워야할 편의점보다 더 적게 생김
    end = mid - 1
    ans = min(ans,mid)
    


print(ans)