import copy
import sys

n = m = 0
arr = []
virusList = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxVal = 0
##DFS로 바이러스 퍼트리기
def spreadVirus(x, y, copyed):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if copyed[nx][ny] == 0:
                copyed[nx][ny] = 2
                spreadVirus(nx, ny, copyed)
## 안전구역 넓이 구하기
def getSafeArea(copyed):
    safe = 0
    for i in range(n):
        for j in range(m):
            if copyed[i][j] == 0:
                safe += 1
    return safe


## 조합으로 벽 3개 놓는 모든 경우 구하기
def setWall(start, depth):
    global maxVal

    if depth == 3:
        # 복사
        copyed = copy.deepcopy(arr)

        length = len(virusList)
        for i in range(length):
            [virusX, virusY] = virusList[i]
            spreadVirus(virusX, virusY, copyed)
            
        maxVal = max(maxVal, getSafeArea(copyed))
        return
        
    for i in range(start, n*m):
        x = (int) (i / m)
        y = (int) (i % m)

        if arr[x][y] == 0:
            arr[x][y] = 1
            setWall(i+1, depth + 1)
            arr[x][y] = 0


if __name__ =='__main__':
    n, m = map(int,sys.stdin.readline().split())
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2: #특이점. 바이러스 발원지를 따로 저장함
                virusList.append([i,j])
    
    ##벽 세우기
    setWall(0, 0)
    print(maxVal)

