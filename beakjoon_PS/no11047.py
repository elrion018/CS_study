N, K = map(int, input().split())
count = 0
coins = []
for _ in range(N):
    coins.append(int(input()))


for i in range(1, N+1):

    if coins[-i] <= K:
        temp = K // coins[-i]
        K -= coins[-i] * temp
        count += temp
print(count)
