import sys

def bs(N,C, arr):
    arr.sort()
    start = 1
    end = arr[-1] - arr[0]
    ans = 0
    while start <= end:
        mid = (start+end) // 2
        prev = 0
        count = 1
        for i in range(1,N):
            if arr[i] - arr[prev] >= mid:
                prev = i
                count += 1
        if count >= C:
            start = mid +1
            ans = mid
        else:
            end = mid -1
    return print(ans)



N, C = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
bs(N,C, arr)