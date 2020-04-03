import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((b, a))
arr = sorted(arr)
cnt = 0
end = 0
for element in arr:
    if element[1] >= end:
        cnt += 1
        end = element[0]
print(cnt)
