N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
for i in range(N-2):
    Sum = 0
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            Sum = cards[i] + cards[j] + cards[k]
            if Sum <= M and M-Sum < M-result:
                result = Sum
print(result)
