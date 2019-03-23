import sys
def close_Store(start, depth, Maxdepth): ##### 가게 폐업 함수
    global Minval
    if depth == Maxdepth:
        copyed = store[:]
        Minval = min(Minval, chi_length(copyed))

    for i in range(start, N*N):
        x = (int) (i / N)
        y = (int) (i % N)
    

        if store[x][y] == 2:
            store[x][y] = 0
            close_Store(x, depth +1, Maxdepth)
            store[x][y] = 2

def chi_length(copyed): ##### 치킨거리 구하는 함수
    temp1 = []
    for i in house_loc:
        x, y = i[0], i[1]
        if copyed[x][y] == 1:
            temp2 = []
            for j in chicken_loc:
                ax, ay = j[0],j[1]
                if copyed[ax][ay] == 2:
                    length = abs((ax-x))+abs((ay-y))
                    temp2.append(length)
            temp1.append(min(temp2))
    City_Length = sum(temp1)
    return City_Length

########
N, M = map(int,sys.stdin.readline().split()) 
store = [] 
for i in range(N):
    store.append(list(map(int,sys.stdin.readline().split())))

Minval = 1000000


chicken = 0 
chicken_loc = []
house_loc = [] 
for i in range(N*N):
    x = (int) (i / N)
    y = (int) (i % N)
    if store[x][y] == 1:
        house_loc.append([x,y])
    if store[x][y] == 2:
        chicken += 1
        chicken_loc.append([x,y])
for i in range((chicken-M), chicken):
    close_Store(0, 0, i)
print(Minval)