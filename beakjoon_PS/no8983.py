import sys

def cal_dist(shoot,animal):
  return abs(shoot - animal[0]) + animal[1]


def bs(arr, animal,l):

  start = 0
  end = len(arr) -1

  while start<= end:
    mid = (start + end) //2

    if arr[mid] <= animal[0]:
      start = mid +1
    
    else:
      end = mid -1

  return end
  

m, n, l = map(int, sys.stdin.readline().split())

arr1 = list(map(int, sys.stdin.readline().split()))

arr2 = []

for _ in range(n):
  arr2.append(list(map(int, sys.stdin.readline().split())))

arr1 = sorted(arr1) # 사대
arr2 = sorted(arr2, key=lambda element: element[0]) #동물

# print(arr1, arr2)

count = 0
for i in range(len(arr2)):
  nearest_shoot_index = bs(arr1, arr2[i], l)

  # print(arr1[nearest_shoot_index], nearest_shoot_index, "call")

  if cal_dist(arr1[nearest_shoot_index], arr2[i]) <= l or (nearest_shoot_index+1 < len(arr1) and cal_dist(arr1[nearest_shoot_index+1], arr2[i]) <= l):
    count += 1

print(count)
  

