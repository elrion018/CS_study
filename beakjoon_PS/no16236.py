def bfs(fishes_count, fishes, shark_yx, baby_size, arr, N):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    min_distance = 999
    min_yx = []
    for fish in fishes:
        queue = [shark_yx]
        visited = [[0]*N for _ in range(N)]
        visited[shark_yx[0]][shark_yx[1]] = 1
        d = 0
        yx = []
        while queue:
            shark_y, shark_x = queue.pop(0)
            if shark_y == fish[0] and shark_x == fish[1]:
                d = visited[shark_y][shark_x]
                yx = [shark_y, shark_x]
                break
            for i in range(4):
                ay = shark_y + dy[i]
                ax = shark_x + dx[i]
                if ay >= 0 and ay < N and ax >= 0 and ax < N:
                    if baby_size >= arr[ay][ax] and visited[ay][ax] == 0:
                        visited[ay][ax] = visited[shark_y][shark_x] + 1
                        queue.append([ay, ax])
        if min_distance > d and yx != []:
            min_distance = d
            min_yx = []
            min_yx.append(yx)
        elif min_distance == d and yx != []:
            min_yx.append(yx)

    return min_yx, (min_distance-1)


def brute_force(arr, N, baby_size):
    fishes_count = 0
    fishes = []
    shark_yx = [0, 0]
    for y in range(N):
        for x in range(N):
            if arr[y][x] < baby_size and arr[y][x] != 0 and arr[y][x] != 9:
                fishes_count += 1
                fishes.append([y, x])
            elif arr[y][x] == 9:
                shark_yx = [y, x]
    return fishes_count, fishes, shark_yx


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
baby_size = 2
time = 0
eat_cnt = 0
while True:
    fishes_count, fishes, shark_yx = brute_force(arr, N, baby_size)
    if fishes_count == 0:
        break
    else:
        min_yx, min_distance = bfs(fishes_count, fishes, shark_yx, baby_size,
                                   arr, N)
        if len(min_yx) != 0:
            min_yx = sorted(min_yx, key=lambda fish: (fish[0], fish[1]))
            target_fish = min_yx.pop(0)
            arr[shark_yx[0]][shark_yx[1]] = 0
            arr[target_fish[0]][target_fish[1]] = 9
            eat_cnt += 1
            if eat_cnt == baby_size:
                baby_size += 1
                eat_cnt = 0
            time += min_distance
        else:
            break
print(time)
