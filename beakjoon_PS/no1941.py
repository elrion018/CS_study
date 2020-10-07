import sys
import collections
sys.setrecursionlimit(10**6)


def bfs(visited1, y, x):
    visited2 = [[False]*5 for _ in range(5)]
    visited2[y][x] = True
    queue = collections.deque()
    queue.append((y, x))
    result = 1
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay >= 0 and ay < 5 and ax >= 0 and ax < 5 and visited1[ay][ax] == True and visited2[ay][ax] == False:
                visited2[ay][ax] = True
                queue.append((ay, ax))
                result += 1

    return result


def dfs(visited, count, S, fy, fx):
    global ans

    if count == 7 and S >= 4:
        if bfs(visited, fy, fx) == 7:
            ans += 1
        return

    elif count == 7:
        return

    for y in range(fy, 5):
        if y == fy:
            for x in range(fx, 5):
                if visited[y][x] == False:
                    visited[y][x] = True
                    if arr[y][x] == "S":
                        dfs(visited, count+1, S+1, y, x)
                    elif arr[y][x] == "Y":
                        dfs(visited, count+1, S, y, x)
                    visited[y][x] = False

        else:
            for x in range(5):
                if visited[y][x] == False:
                    visited[y][x] = True
                    if arr[y][x] == "S":
                        dfs(visited, count+1, S+1, y, x)
                    elif arr[y][x] == "Y":
                        dfs(visited, count+1, S, y, x)
                    visited[y][x] = False


arr = [list(sys.stdin.readline().strip()) for _ in range(5)]
temp = 0
ans = 0
visited = [[False]*5 for _ in range(5)]
dfs(visited, 0, 0, 0, 0)

print(ans)
