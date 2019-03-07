#이분 탐색 사용시
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

N = int(input())
AN = merge_sort(map(int,input().split()))
M = int(input())
AM = list(map(int,input().split()))

for i in AM:
    start = 0
    end = len(AN) -1
    while True:
        mid = (start+end)//2
        if AN[mid] == i:
            print(1)
            break
        elif start == end and AN[mid] != i:
            print(0)
            break
        elif AN[mid] < i:
            start = mid +1
        else:
            end = mid - 1


# set사용시

N = int(input())
AN = set(map(int,input().split()))
M = int(input())
for _ in map(int,input().split()):
    print(1 if _ in AN else 0)