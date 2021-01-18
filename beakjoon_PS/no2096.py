import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


one = arr[0][0]
two = arr[0][1]
thr = arr[0][2]

for y in range(1, N):
    temp_one = max(one, two) + arr[y][0]
    temp_two = max(one, two, thr) + arr[y][1]
    temp_thr = max(two, thr) + arr[y][2]
    one = temp_one
    two = temp_two
    thr = temp_thr

maxVal = max(one, two, thr)


one = arr[0][0]
two = arr[0][1]
thr = arr[0][2]

for y in range(1, N):
    temp_one = min(one, two) + arr[y][0]
    temp_two = min(one, two, thr) + arr[y][1]
    temp_thr = min(two, thr) + arr[y][2]
    one = temp_one
    two = temp_two
    thr = temp_thr

minVal = min(one, two, thr)

print(maxVal, minVal)
