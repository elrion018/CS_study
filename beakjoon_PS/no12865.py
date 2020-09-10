# D[i][j] i번째 물건까지 넣었고 무게가 j일때 물건들의 가치합
# 물건 I
# j >= I[i-1][0] 일떄
# D[i][j] = max(D[i-1][j], D[i-1][j-I[i-1][0]] + I[i-1][1])
# 아닐 때
#D[i][j] = D[i-1][j]
# 밑에 식은, 내가 넣을 수 있는 물품이 있는데, 그 물품을 배낭에 넣었을 때 최대 무게를 초과한다면 benefit(가치)를 추가하지 않고 이전 benefit(가치)를 그대로 가져오겠다는 것이다.
# 위에 식은, 나에게 새로운 물품이 있고 최대 무게를 넘어서지 않는다는 것이다. 이제 이전 benefit(가치)와 이전 것의 물품을 빼고 내가 새로 받은 물품의 가치를 넣었을 때의 가치를 비교해서 더 큰 것을 취한다.
import sys
N, K = map(int, sys.stdin.readline().split())
I = []
maxVal = -sys.maxsize
for _ in range(N):
    I.append(list(map(int, sys.stdin.readline().split())))

D = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= I[i-1][0]:
            D[i][j] = max(D[i-1][j], D[i-1][j-I[i-1][0]] + I[i-1][1])
        else:
            D[i][j] = D[i-1][j]
        if maxVal < D[i][j]:
            maxVal = D[i][j]
print(maxVal)
