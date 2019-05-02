def BFS(xy, col):
    queue = [xy]
    while True:
        if len(queue) == 0:
            break
        bx, by = queue.pop(0)
        for i in range(4):
            ax = bx + cx[i]
            ay = by + cy[i]
            if ax>=0 and ax <N and ay>=0 and ay<N:
                if grid[ax][ay] == col and visited[ax][ay] !=1:
                    queue.append([ax,ay])
                    visited[ax][ay] = 1
def BFS2(xy, col):
    queue = [xy]
    while True:
        if len(queue) == 0:
            break
        bx, by = queue.pop(0)
        for i in range(4):
            ax = bx + cx[i]
            ay = by + cy[i]
            if ax>=0 and ax <N and ay>=0 and ay<N:
                if grid2[ax][ay] == col and visited2[ax][ay] !=1:
                    queue.append([ax,ay])
                    visited2[ax][ay] = 1


###입력
N = int(input())

grid = [] #그리드 선언
for i in range(N):
    grid.append((','.join(input())).split(','))

        

### 방문 체크 리스트 선언
visited = [[0]*N for i in range(N)]
visited2 = [[0]*N for i in range(N)]
# print(visited)

### 큐 선언
queue = []

### 방향 전환 리스트 선언
cx = [0,0,-1,1]
cy = [-1,1,0,0]

### 색깔리스트 선언
color = ['R','G','B']

### 완전 탐색 - 비 적록색약
count = 0 # 구역 갯수를 담을 변수 - 비적록색약
for i in range(N):
    for j in range(N):
        if grid[i][j] in color and visited[i][j] != 1:
            col = grid[i][j]
            visited[i][j] = 1
            count += 1
            BFS([i,j], col)

### 그리드의 적녹색을 일치시켜주기
count2 = 0 # 구역 갯수를 담을 변수 - 적록색약
grid2= grid[:]
for i in range(N):
    for j in range(N):
        if grid2[i][j] == 'G':
            grid2[i][j] = 'R'

### 완전탐색 - 적록색약   
for i in range(N):
    for j in range(N):
        if grid2[i][j] in color and visited2[i][j] != 1:
            col = grid2[i][j]
            visited2[i][j] = 1
            count2 += 1
            BFS2([i,j], col)

### 비적록색약, 적록색약 값 출력
print(count, count2)