import sys


def bs(arr, h):
    st = 0
    end = len(arr) - 1

    while end >= st:
        mid = (st + end) // 2
        if arr[mid] <= h:
            st = mid + 1
        else:
            end = mid - 1
    return len(arr) - (end + 1)


N, H = map(int, sys.stdin.readline().split())

up_list = []
down_list = []

for i in range(N):
    if i % 2 == 0:
        down_list.append(int(sys.stdin.readline()))
    else:
        up_list.append(int(sys.stdin.readline()))


cnt = 0
minVal = sys.maxsize

up_list.sort()
down_list.sort()
for h in range(1, H+1):
    up_cnt = bs(up_list, h-1)
    down_cnt = bs(down_list, H-h)
    if minVal > up_cnt + down_cnt:
        minVal = up_cnt + down_cnt
        cnt = 1
    elif minVal == up_cnt + down_cnt:
        cnt += 1

print(minVal, cnt)
