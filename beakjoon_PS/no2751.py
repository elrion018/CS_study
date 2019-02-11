import sys
def mergeSort(x):
    if len(x) < 2:
        return x
    mid = len(x) // 2
    left = x[:mid]
    right = x[mid:]
    leftList = mergeSort(left)
    rightList = mergeSort(right)
    return merge(leftList, rightList)

def merge(left,right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right = right[1:]
            elif left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
        elif len(left) >0:
            result.append(left[0])
            left = left[1:]
        elif len(right) >0:
            result.append(right[0])
            right = right[1:]
    return result
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num not in lst:
        lst.append(num)
for j in mergeSort(lst):
    print(j)

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num not in lst:
        lst.append(num)
for j in sorted(lst):
    print(j)
#시간초과를 도저히 해결 못하겠음.