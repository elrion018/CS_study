T = int(input())
for i in range(T):
    H,W = list(map(int,input().split()))
    for j in range(H):
        a = input()
        b = W-1
        while b>=0:
            print(a[b], end='')
            b -= 1
        print()

        