##############################
#백준1149번입니다. dp를 활용해서 풀었습니다.
#2019-04-07
##############################

N = int(input())
D = []
C = []
ans = 0
for i in range(N):
    if i==0:
        C.append(list(map(int,input().split())))
        D.append(C[0])
    if i==1:
        C.append(list(map(int,input().split())))
        a = min(D[0][1], D[0][2]) + C[1][0]
        b = min(D[0][0], D[0][2]) + C[1][1]
        c = min(D[0][0], D[0][1]) + C[1][2]
        D.append([a,b,c])
    if i>=2:
        C.append(list(map(int,input().split())))
        D.append([0,0,0])
        D[i][0] =min(D[i-1][1], D[i-1][2]) + C[i][0]
        D[i][1] =min(D[i-1][0], D[i-1][2]) + C[i][1]
        D[i][2] =min(D[i-1][0], D[i-1][1]) + C[i][2]
ans = min(D[N-1][0], D[N-1][1], D[N-1][2])
print(ans)