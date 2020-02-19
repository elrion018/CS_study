# 입력( 갯수 N, x,y 시작점, d 시작 방향, g 세대)

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

# dy, dx 생성 0 동 1 북 2 서 3 남

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

# 격자 생성
grid = [[0]*101 for _ in range(101)]

# 드래곤커브 생성

for x, y, d, g in info:
    # 세대만큼 생성 방향 생성
    d_array = [d]
    for _ in range(g):
        temp2 = []
        for i in range(len(d_array)-1, -1, -1):
            if (d_array[i]+1 == 4):
                temp2.append(0)
            else:
                temp2.append(d_array[i]+1)
        d_array.extend(temp2)

    # 세대만큼 드래곤 커브 생성
    grid[y][x] = 1  # 시작점 칠하기
    for i in d_array:
        ay = y + dy[i]
        ax = x + dx[i]
        if ax >= 0 and ay >= 0 and ax < 101 and ay < 101:
            grid[ay][ax] = 1
            x = ax
            y = ay

# 완전탐색으로 드래곤커브에 속하는 정사각형 알아내기.

count = 0  # 정사각형 갯수 누적
for i in range(0, 100):
    for j in range(0, 100):
        if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1]:
            count += 1
print(count)
