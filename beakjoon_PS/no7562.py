###BFS
def BFS(minVal):
    ###처음 8가지 방향에 따라 각각 BFS
    for i in range(8):
        fx = sx + cx[i]
        fy = sy + cy[i]
        if fx>=0 and fx<leng and fy>=0 and fy<leng:
            chess[fx][fy] = 1
            queue.append([fx,fy])
    
    while len(queue)!=0:
        bx, by = queue.pop(0)
        if bx == ex and by == ey:
            if minVal > chess[bx][by]:
                minVal = chess[bx][by]
            continue
        for i in range(8):
            ax = bx +cx[i]
            ay = by +cy[i]
            if ax>=0 and ax<leng and ay>=0 and ay<leng:
                if chess[bx][by]+1>=minVal:
                    continue
                if chess[ax][ay] == 0:
                    chess[ax][ay] = chess[bx][by] +1
                    queue.append([ax,ay])
                else:
                    if chess[bx][by]+1 < chess[ax][ay]:
                        chess[ax][ay] = chess[bx][by]+1
                        queue.append([ax,ay])
    return minVal




###입력
tc = int(input())

###queue 선언
queue = []

###이동 방향 선언
cx = [-1,-2,-2,-1,1,2,2,1]
cy = [-2,-1,1,2,2,1,-1,-2]

###x테케 수만큼 for 문
for _ in range(tc):
    _list = []
    #체스판 한 변 길이 입력
    leng = int(input())
    #체스판 만들기
    chess = [[0]*leng for _ in range(leng)]
    #나이트의 현재 칸, 이동하려는 칸 입력
    sx, sy = list(map(int,input().split()))
    ex, ey = list(map(int, input().split()))
    if sx == ex and sy == ey:
        print(0)
    else:
        print(BFS(99999999))