result = 0
N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if arr[i] >= arr[j]:
            temp = arr[i] - arr[j]
        else:
            temp = arr[j] - arr[i]
        result += temp
print(result)
