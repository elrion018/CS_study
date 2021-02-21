import sys

while True:
    n, m = sys.stdin.readline().split()
    n = int(n)
    m = float(m)
    if n == 0 and m == 0.00:
        break
    m = int(m*100+0.5)
    dp = [0]*(m+1)
    arr = []
    for _ in range(n):
        c, p = sys.stdin.readline().split()
        c = int(c)
        p = int(float(p)*100+0.5)
        arr.append([c, p])
    for j in range(n):
        for i in range(arr[j][1], m+1):
            dp[i] = max(dp[i], dp[i-arr[j][1]] + arr[j][0])

    print(dp[m])
