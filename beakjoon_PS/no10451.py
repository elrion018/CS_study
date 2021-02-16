import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    check = [0] * (N+1)
    ans = 0

    for i in range(1, N+1):
        temp = []
        if check[arr[i]] == 0:
            temp.append(arr[i])
            st = arr[i]
            mid = arr[i]
            while True:
                if arr[mid] == st:
                    temp.append(mid)
                    ans += 1
                    break
                else:
                    temp.append(mid)
                    mid = arr[mid]
            for vec in temp:
                check[vec] = 1
    print(ans)
