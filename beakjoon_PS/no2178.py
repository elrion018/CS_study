N, M = map(int,input().split())
maze = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        maze[i][j] = int(temp[j])

dN = [0,0,1,-1]
dM = [-1,1,0,0]
queue = [(0,0)]
visited[0][0] = 1

while queue:
    bN, bM = queue.pop(0)
    if N-1 == bN and M-1 == bM:
        print(visited[bN][bM])
        break
    for i in range(4):
        aN = bN + dN[i]
        aM = bM + dM[i]
        if aN >= 0 and aN <N and aM >= 0 and aM <M:
            if visited[aN][aM] == 0 and maze[aN][aM] == 1:
                visited[aN][aM] = visited[bN][bM] + 1
                queue.append((aN,aM))
