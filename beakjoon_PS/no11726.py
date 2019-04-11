n = int(input())
D = [0,1,2]
if n == 1:
    print(D[1])
if n == 2:
    print(D[2])
if n >= 3:
    for i in range(3,n+1):
        D.append(0)
        D[i] = D[i-1] + D[i-2]
    print(D[n] % 10007)
