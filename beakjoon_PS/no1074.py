import sys

N, r, c = map(int, sys.stdin.readline().split())

y = (2**N) / 2
x = y

ans = 0

while N:
    move = (2**(N-1))/2
    check = 4**(N-1)
    if r < y and c < x:  # 1
        y -= move
        x -= move
    elif r < y and c >= x:  # 2
        y -= move
        x += move
        ans += check

    elif r >= y and c < x:  # 3
        y += move
        x -= move
        ans += check * 2

    elif r >= y and c >= x:  # 4
        y += move
        x += move
        ans += check * 3
    N -= 1

print(ans)
