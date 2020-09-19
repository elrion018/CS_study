import sys
import collections


def bfs(N, K):
    visited = [0] * 100001
    queue = collections.deque()
    queue.append(N)
    visited[N] = 1

    while queue:
        X = queue.popleft()
        if X == K:
            return print(visited[K]-1)
        if X*2 >= 0 and X*2 < 100001 and visited[X*2] == 0:
            visited[X*2] = visited[X]
            queue.append(X*2)
        if X - 1 >= 0 and X - 1 < 100001 and visited[X-1] == 0:
            visited[X-1] = visited[X] + 1
            queue.append(X-1)
        if X + 1 >= 0 and X + 1 < 100001 and visited[X+1] == 0:
            visited[X+1] = visited[X] + 1
            queue.append(X+1)


N, K = map(int, sys.stdin.readline().split())
bfs(N, K)
