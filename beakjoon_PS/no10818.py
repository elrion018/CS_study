import sys
minVal = sys.maxsize
maxVal = -sys.maxsize

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if minVal > arr[i]:
        minVal = arr[i]
    if maxVal < arr[i]:
        maxVal = arr[i]
print(minVal, maxVal)
