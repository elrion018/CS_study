###BFS
def BFS(xy):
    queue = [xy]
    while len(queue) != 0:
        bx, by = queue.pop(0)
        
        for i in range(4):
            ax = bx + cx[i]
            ay = by + cy[i]
            if ax>=0 and ax<M and ay>=0 and ay<N:
                if area[ay][ax] == 1 and visited[ay][ax] == 0:
                    visited[ay][ax] = 1
                    queue.append([ax,ay])





###입력
T = int(input())

###queue 선언
queue = []

###이동 방향 선언
cx = [0,0,-1,1]
cy = [-1,1,0,0]

#테케 만큼 반복
for _ in range(T):
    M, N, K = list(map(int,input().split()))
    #배추 밭 생성
    area = [[0]*M for _ in range(N)]

    #방문 체크 리스트 만들기
    visited = [[0]*M for _ in range(N)]

    #K만큼 반복하며 배추 밭에 배추 위치 기록하기
    for __ in range(K):
        x, y =list(map(int,input().split()))
        area[y][x] = 1
    #지렁이 마릿수를 저장할 변수 선언
    worms = 0
    for y in range(N):
        for x in range(M):
            if area[y][x] == 1 and visited[y][x] == 0:

                visited[y][x] = 1
                worms += 1
                BFS([x,y])

    print(worms)

