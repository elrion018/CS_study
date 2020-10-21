import bisect
import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))

arr1.sort()
ans = sys.maxsize
a1, a2, a3 = 0, 0, 0

for i in range(n):
    for j in range(i+1, n):
        r = bisect.bisect_left(arr1, -(arr1[i] + arr1[j]))
        l = r-1
        if r == i or r == j:
            r += 1
            if r == i or r == j:
                r += 1
        if l == i or l == j:
            l -= 1
            if l == i or l == j:
                l -= 1
        if 0 <= r and r < n and abs((arr1[i]+arr1[j]) + arr1[r]) < ans:
            ans = abs((arr1[i]+arr1[j]) + arr1[r])
            a1, a2, a3 = i, j, r
        if 0 <= l and l < n and abs((arr1[i] + arr1[j]) + arr1[l]) < ans:
            ans = abs((arr1[i]+arr1[j]) + arr1[l])
            a1, a2, a3 = i, j, l
print(arr1[a1], end=' ')
print(arr1[a2], end=' ')
print(arr1[a3])
