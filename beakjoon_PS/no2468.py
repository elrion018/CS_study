###BFS
def BFS(xy):
    queue = [xy]
    while len(queue) != 0:
        bx, by = queue.pop(0)
        for i in range(4):
            ax = bx + cx[i]
            ay = by + cy[i]
            if ax>=0 and ax<N and ay>=0 and ay<N:
                if area[ay][ax] > rain and visited[ay][ax] == 0:
                    visited[ay][ax] = 1
                    queue.append([ax,ay])



###최대 강수량 담는 변수 선언
maxRain = 0

###큐 선언
queue = []

###이동 방향 선언
cx = [0,0,-1,1]
cy = [-1,1,0,0]


###입력
N = int(input())


#지역 리스트 선언
area = []
for _ in range(N):
    _input = list(map(int,input().split()))
    maxInput = max(_input)
    #최대 강수량 갱신해주기
    if maxInput > maxRain:
        maxRain = maxInput
    area.append(_input)

###최대 강수량으로 for문 돌리기
resultList = [] #안전 구역 갯수를 최종 비교해주기위한 리스트 선언
for rain in range(0,maxRain+1):
    visited = [[0]*N for _ in range(N)] #방문 체크용
    safeCount = 0 #안전 영역의 갯수를 저장하는 변수 선언
    for y in range(N):
        for x in range(N):
            if area[y][x] > rain and visited[y][x] == 0:
                safeCount += 1
                visited[y][x] = 1
                BFS([x,y])
                
    resultList.append(safeCount)
print(max(resultList))
