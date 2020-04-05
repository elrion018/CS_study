import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
acc = 0
result = 0
for i in arr:
    acc += i
    result += acc
print(result)
