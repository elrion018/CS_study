import sys

def solution(n, m, arr):
    start = 0
    end = max(arr)

    

    while start<= end:
      mid = (start+end) // 2
      sum_budget = 0

      for i in range(n):
        if arr[i] >= mid:
          sum_budget += mid

        else:
          sum_budget += arr[i]
      
      if sum_budget <= m:
        start = mid + 1

      else:
        end = mid -1
    
    return end




n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

print(solution(n,m,arr))
