import sys
import collections
result = None
count = 0


def bfs(N, K):
    global result, count
    visited = [0] * 100001
    queue = collections.deque()
    queue.append(N)
    visited[N] = 1

    while queue:
        X = queue.popleft()
        if X == K:
            if result is None:
                result = visited[K] - 1
                count += 1
            else:
                if result == visited[K]-1:
                    visited[K] = 0
                    count += 1

        if X*2 >= 0 and X*2 < 100001 and (visited[X*2] == 0 or X*2 == K):
            visited[X*2] = visited[X] + 1
            queue.append(X*2)
        if X - 1 >= 0 and X - 1 < 100001 and (visited[X-1] == 0 or X-1 == K):
            visited[X-1] = visited[X] + 1
            queue.append(X-1)
        if X + 1 >= 0 and X + 1 < 100001 and (visited[X+1] == 0 or X+1 == K):
            visited[X+1] = visited[X] + 1
            queue.append(X+1)


N, K = map(int, sys.stdin.readline().split())
bfs(N, K)
print(result)
print(count)
