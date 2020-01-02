M, N = map(int, input().split())
if N - 45 < 0:
    temp = N - 45
    N = 60 + temp
    if M - 1 >= 0:
        M -= 1
    else:
        M = 23
else:
    N = N - 45
print(M, N)
