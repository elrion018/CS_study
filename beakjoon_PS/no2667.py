def search(x):
    queue =[x]
    di = [0,0,1,-1]
    dj = [-1,1,0,0]
    count = 1
    visit[x[0]][x[1]] = 1
    while queue:
        (ci, cj) = queue.pop(0)
        for k in range(4):
            ai = ci + di[k]
            aj = cj + dj[k]
            if ai >= 0 and ai <Size and aj >=0 and aj <Size:
                if visit[ai][aj] == 0 and Map[ai][aj] == 1:
                    visit[ai][aj] = 1
                    count +=1
                    queue.append((ai,aj))
    result.append(count)
    return None

Size = int(input())
visit = [[0]*Size for _ in range(Size)]
Map = [[0]*Size for _ in range(Size)]
for i in range(Size):
    temp = input()
    for j in range(Size):
        Map[i][j] = int(temp[j])

result = []
count2 = 0
for i in range(Size):
    for j in range(Size):
        if visit[i][j] == 0 and Map[i][j] == 1:
            count2 +=1
            search((i,j))
print(count2)
for i in sorted(result):
    print(i)