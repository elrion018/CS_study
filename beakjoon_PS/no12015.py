import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

D = [[] for _ in range(N)]

for i in range(len(arr)):
    D[i].append(arr[i])
for i in range(N):
    for j in range(i, -1, -1):
        if arr[i] > arr[j] and len(D[j]) >= len(D[i]):
            temp = []
            for k in D[j]:
                temp.append(k)
            temp.append(arr[i])
            D[i] = temp
result = (max(D, key=lambda element: len(element)))
print(len(result))
print(" ".join(map(str, result)))
