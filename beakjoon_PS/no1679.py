###연산함수
def cal(bN, i):
    if i == 0:
        return bN-1
    elif i == 1:
        return bN+1
    elif i == 2:
        return bN*2

###BFS
def BFS(minVal,N,K):
    queue = [N]
    while len(queue) != 0:
        bN = queue.pop(0)

        if bN == K:
            if visited[bN] < minVal:
                minVal = visited[bN]
            continue
        
        for i in range(3):
            aN = cal(bN, i)

            if visited[bN] + 1 >= minVal:
                continue
            
            if aN>=0 and aN<len(nkList):
                if visited[aN] == 0:
                    visited[aN] = visited[bN] + 1
                    queue.append(aN)
                else:
                    if visited[bN]+1<visited[aN]:
                        visited[aN] = visited[bN] +1
                        queue.append(aN)
    return minVal




###입력

N, K = list(map(int,input().split()))

###큐 선언
queue = []

###N, K가 포함된 리스트 선언
if N > K:
    nkList = [i for i in range(N+3)]

elif N < K:
    nkList = [i for i in range(K+3)]
elif N == K:
    nkList = [1]





##체크리스트 선언
visited = [0 for _ in range(len(nkList))]



##탐색시작
if N == K:
    print(0)
else:
    print(BFS(999999,N,K))
