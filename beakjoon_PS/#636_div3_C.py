import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    sumVal = 0
    maxVal = -sys.maxsize
    for i in range(n):
        maxVal = max(maxVal, arr[i])
        if i == n-1:
            sumVal += maxVal
        elif arr[i]*arr[i+1] < 0:
            sumVal += maxVal
            maxVal = arr[i+1]
    print(sumVal)
