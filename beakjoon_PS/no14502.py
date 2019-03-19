import copy

def spreadVirus(x):
    dN = [0,0,1,-1]
    dM = [-1,1,0,0]
    queue = [x]

    while queue:
        bN, bM = queue.pop(0)
        for i in range(4):
            aN = bN + dN[i]
            aM = bM + dM[i]
            if aN >= 0 and aN <N and aM>=0 and aM<M:
                if Map_Walls[aN][aM] == 0 and Map[aN][aM] == 0:
                    Map_Walls[aN][aM] = 2
                    queue.append((aN,aM))



N, M =map(int, input().split())
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))

Map_Walls = copy.deepcopy(Map)
temp = copy.deepcopy(Map_Walls) #temp에 '복사'해주자
result = []
for a in range(0, N*M):
    x = (int) (a / M)
    y = (int) (a % M)
    Map_Walls = copy.deepcopy(temp) # 기록을 벽 0개인 때로 초기화해주자
    if Map_Walls[x][y] == 0 and Map[x][y] ==0: #기록에도, 실제로도 벽이 없음 세우자
        Map_Walls[x][y] = 1 #벽 1개 째 세운다.            
        temp2 = copy.deepcopy(Map_Walls)#벽이 1개인 상태를 저장해준다.

        for b in range(0, N*M):
            x = (int) (b / M)
            y = (int) (b % M)
            Map_Walls = copy.deepcopy(temp2) #벽이 1개인 상태로 초기화해준다.
            if Map_Walls[x][y] == 0 and Map[x][y] ==0:
                Map_Walls[x][y] = 1 #벽 2개째 세운다.
                temp3 = copy.deepcopy(Map_Walls) #벽이 2개인 상태를 저장해준다.

                for c in range(0, N*M):
                    x = (int) (c / M)
                    y = (int) (c % M)
                    Map_Walls = copy.deepcopy(temp3)
                    if Map_Walls[x][y] == 0 and Map[x][y] == 0:
                        Map_Walls[x][y] = 1
                        safety_area = 0
                        for d in range(0, N*M):
                            x = (int) (d / M)
                            y = (int) (d % M)
                            if Map_Walls[x][y] == 2 and Map[x][y] == 2:
                                spreadVirus((x,y))
                                    
                        for e in range(0, N*M):
                            x = (int) (e / M)
                            y = (int) (e % M)
                            if Map_Walls[x][y] == 0:
                                safety_area += 1
                        result.append(safety_area)
                                    
result = list(set(result))
print(max(result))