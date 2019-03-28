#####################################
# programing date : 2019-03-27
# 복습필요
#####################################

from collections import deque #블록을 담기 위한 덱

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)] #보드 내려받기

ans, q = 0, deque() #계속 갱신할 정답과 블록을 담을 덱을 준비

def cal(cnt): #방향이동 횟수를 저장할 cnt
    global ans, board #계속 바꿔줄 ans와 board는 전역변수로 설정해주자.

    if cnt == 5: #5번째 이동까지 다하면
        for i in range(n):
            ans = max(ans,max(board[i])) #최댓값 갱신
        return

    copy = [c[:] for c in board] #보드 초기화를 위해 이동 이전 보드형태 복사 
    
    for i in range(4): #네 방향 이동
        move(i)
        cal(cnt + 1) #이동 횟수 누적
        board = [c[:] for c in copy] #보드 초기화 해주기(이동 이전으로)

def get(i, j): #블록 담는 메소드
    if board[i][j]: #블록이 존재한다면 담기.
        q.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj):
    while q: #q가 있는동안
        block = q.popleft() #큐에서 블록 꺼내기
        if not board[i][j]: #보드자리가 비어있다면 블록 넣어주기
            board[i][j] = block
        elif board[i][j] == block: #보드자리에 있는 블록이 넣으려는 블록과 같다면 합쳐주기
            board[i][j] = block*2
            i, j = i+di, j+dj #합쳤으므로 보드자리 바꿔주기
        else: #아무 해당사항이 없으면 보드자리 바꿔서 넣어주기
            i, j = i+di, j+dj
            board[i][j] = block


def move(x): #블록 움직이는 메소드
    if x == 0: #위로 이동
        for j in range(n): #열
            for i in range(n): #행
                get(i,j)
            # print(i,j)
            merge(0, j, 1, 0)
    elif x == 1: #아래로 이동
        for j in range(n): #열
            for i in range(n-1,-1,-1): #행
                get(i,j)
            merge(n-1, j, -1, 0)
    elif x == 2: #왼쪽으로 이동
        for i in range(n): #행
            for j in range(n): #열
                get(i,j)
            merge(i, 0, 0, 1)
    elif x == 3: #오른쪽으로 이동
        for i in range(n): #행
            for j in range(n-1,-1,-1):
                get(i,j)
            merge(i, n-1, 0, -1)
cal(0)
print(ans)
    
    


