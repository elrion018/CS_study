def BFS(i, graph, N):
    # 큐 선언, 방문 배열 선언
    queue = [i]
    visited = [0] * N

    # 큐가 빌 때까지 반복
    while queue:
        index = queue.pop(0)
        for i, v in enumerate(graph[index]):
            if visited[i] == 0 and v == 1:
                visited[i] = 1
                queue.append(i)
    return ' '.join(map(str, visited))


# 입력
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 정점들 마다 BFS
for i in range(N):
    print(BFS(i, graph, N))
