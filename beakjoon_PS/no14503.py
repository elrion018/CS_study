import sys
N, M = list(map(int,sys.stdin.readline().split()))
r, c, d = list(map(int,sys.stdin.readline().split()))
#북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

##청소구역 계산함수
def countClean():
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 1:
                count+= 1
    return count

##회전 함수
def turn(d):
    if d == 0:
        return 3
    else:
        return d-1
        
##청소 함수
def clean(x,y):
    arr[x][y] = 2

##메인 함수
def runner(x, y, d, turnCount):
    while True: #끝날 때 까지 무한 반복 필요.

        #2.3 네 방향 모두 청소가 되어있거나 벽인 경우
        if turnCount == 4:
            backX = x - dx[d]
            backY = y - dy[d]
            #후진할 자리에 벽이있다면
            if arr[backX][backY] == 1:
                print(countClean())
                return
            #후진할 자리에 벽이 없다면
            else:
                x, y, d, turnCount = backX, backY, d, 0
                

        #1.1 현재 위치를 청소한다.
        if arr[x][y] == 0:
            clean(x, y)

        #2현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색진행
        
        td = turn(d)
        ax = x + dx[td]
        ay = y + dy[td]
        ##2.1왼쪽 방향에 청소하지 않은 공간이 존재한다면
        if arr[ax][ay] == 0:
            x, y, d, turnCount = ax, ay, td, 0
        ##2.2 왼쪽 방향에 청소할 공간이 없다면     
        else:
            x, y, d, turnCount = x, y, td, turnCount + 1

runner(r, c, d, 0)