def BFS(x):
    queue.append(x)
    size = 1
    while True:
        if len(queue) == 0:
            break
        bx, by = queue.pop()
        for i in range(4):
            ax = bx + cx[i]
            ay = by + cy[i]
            if ax >= 0 and ax <nums[0] and ay >= 0 and ay < nums[1]:
                if check[ax][ay] == 0 and pictures[ax][ay] ==1:
                    check[ax][ay] = 1
                    size += 1
                    queue.append((ax, ay))
    return size

###########입력
nums = list(map(int,input().split()))

pictures = [list(map(int,input().split())) for _ in range(nums[0])]
check = [[0]*nums[1] for _ in range(nums[0])]

###########큐 선언

queue = []

###########방향 이동 선언
cx = [0,0,-1,1]
cy = [-1,1,0,0]

###########완전 탐색
count = 0 # 그림 숫자 담는 변수
_list = []# 그림 크기 담는 리스트
for i in range(nums[0]):
    for j in range(nums[1]):
        if pictures[i][j] == 1 and check[i][j] == 0:
            count += 1
            check[i][j] =1
            _list.append(BFS((i,j)))

################출력

print(count)
if count == 0:
    print(0)
else:
    print(max(_list))