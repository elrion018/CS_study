#############
#백준 2579번입니다 dp로 풀었습니다.
#2019-04-06
#############


#### 입력받기(N, S)
N = int(input())
S = [int(input()) for _ in range(N)]

#### D 테이블 만들기

D = [0,0]

if N == 1:
    D[0] = [S[0],0]
if N == 2:
    D[0] = [S[0],0]
    D[1] = [S[1],S[0]+S[1]]


#### dp 점화식
if N >=3:
    D[0] = [S[0],0]
    D[1] = [S[1],S[0]+S[1]]
    for i in range(2,N):
        D.append([0, 0])
        D[i][0] = max(D[i-2][0], D[i-2][1]) + S[i]
        D[i][1] = D[i-1][0] + S[i]
ans = max(D[N-1][0],D[N-1][1])
print(ans)