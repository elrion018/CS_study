import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr = sorted(arr, key= lambda element: (element[1], element[0]))

end = 0

cnt = 0
for element in arr:
  if element[0] >= end:
    cnt += 1
    end = element[1]


print(cnt)