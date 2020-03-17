K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
start = 1
end = max(lines)
ans = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in lines:
        temp += (i//mid)
    if temp >= N:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)
