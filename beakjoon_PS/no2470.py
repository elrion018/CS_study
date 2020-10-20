import bisect
import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))

arr1.sort()
ans = 30000000000
a1, a2 = 0, 0

for i in range(n):
    r = bisect.bisect_left(arr1, -arr1[i])
    l = r-1
    if r == i:
        r += 1
    if l == i:
        l -= 1

    if 0 <= r and r < n and abs(arr1[i]+arr1[r]) < ans:
        ans = abs(arr1[i]+arr1[r])
        a1, a2 = i, r
    if 0 <= l and l < n and abs(arr1[i]+arr1[l]) < ans:
        ans = abs(arr1[i]+arr1[l])
        a1, a2 = i, l

print(arr1[a1], end=' ')
print(arr1[a2])
