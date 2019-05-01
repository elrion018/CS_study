def BFS(x):
    size = 1 #영역 크기 저장 변수
    queue = [x]
    while True:
        if len(queue) == 0:
            break
        bx, by = queue.pop(0)
        for i in range(4):
            ax = bx + cx[i]
            ay = by + cy[i]
            if ax >= 0 and ax <M and ay >= 0 and ay <N:
                if paper[ax][ay] == 0 and visited[ax][ay] != 2:
                    visited[ax][ay] = 2
                    queue.append([ax,ay])
                    size += 1
    return size



###입력
M, N, K = list(map(int,input().split()))

###빈 종이 선언
paper = [[0]*N for _ in range(M)]
# print(paper)

###사각형 좌표 입력
xy = []
for i in range(K):
    lx, ly, rx, ry = list(map(int,input().split()))
    for j in range(ly, ry):
        for k in range(lx, rx):
            if paper[j][k] != 1:
                paper[j][k] = 1

###체크용 리스트 선언
visited = paper[:]

### 큐 선언
queue = []

### 방향이동 선언
cx = [0,0,-1,1]
cy = [-1,1,0,0]

### 각 영역의 넓이 저장할 리스트 선언
_list = []
###종이에 완전탐색 돌리기
count = 0 #영역 갯수 저장 변수
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0 and visited != 2:
            visited[i][j] = 2
            _list.append(BFS([i,j]))
            count += 1
print(count)
print(" ".join(map(str,sorted(_list))))