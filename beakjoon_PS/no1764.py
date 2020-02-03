N, M = map(int, input().split())
arr1 = set(input() for _ in range(N))
arr2 = set(input() for _ in range(M))
result = list(arr1 & arr2)

print(len(result))
for k in sorted(result):
    print(k)
