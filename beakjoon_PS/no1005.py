import sys
def get(x):
        if dp[x] != None:
           return dp[x]

        st = 0

        for y in req[x]:
           st = max(st, get(y))

        dp[x] = st + cost[x]
        
        return dp[x]

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    req = [ [] for _ in range(n+1) ]

    for _ in range(k):
        x, y = map(int, input().split())
        req[y].append(x)
        
    dp = [None] * (n+1)
    
    print(get(int(input())))