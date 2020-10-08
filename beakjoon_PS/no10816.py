import sys
import bisect


N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for element in arr2:
    temp = bisect.bisect_right(arr1, element) - \
        bisect.bisect_left(arr1, element)
    print(temp, end=' ')
