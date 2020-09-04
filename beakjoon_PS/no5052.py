import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []

    for _ in range(n):
        arr.append(sys.stdin.readline()[:-1])

    arr.sort()
    for i in range(n):
        prefix = arr[i]
        if i == n-1:
            print("YES")
            break

        if len(arr[i+1]) >= len(prefix):
            if prefix == arr[i+1][:len(prefix)]:
                print("NO")
                break
