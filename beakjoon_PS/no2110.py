def solve(arr, N, C):
    arr.sort()
    start = 1
    end = arr[N-1] - arr[0]
    d = 0
    ans = 0

    while start <= end:
        first = arr[0]
        mid = (start + end) // 2
        cnt = 1
        for i in range(1, N):
            d = arr[i] - first
            if (mid <= d):
                cnt += 1
                first = arr[i]

        if cnt >= C:
            ans = mid
            start = mid + 1

        else:
            end = mid - 1
    return print(ans)


N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

solve(arr, N, C)
