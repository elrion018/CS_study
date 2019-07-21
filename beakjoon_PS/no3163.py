#충돌하는 경우의 함수
def crash(i, j):
    arr[i][1] = -arr[i][1]
    arr[j][1] = -arr[j][1]

#행진하게하는 함수
def move(x):
    #개미의 id가 양수일 때
    if x[1] >= 0:
        x[0] += 1
        return x

    #개미의 id가 음수 일 때
    else:
        x[0] -= 1
        return x
    
T = int(input())
for _ in range(T):
    N, L, k = list(map(int,input().split()))
    #막대 어레이 선언
    arr =[]
    #떨어진 개미 id 어레이 선언
    fallenId = []
    for _ in range(N):
        p, a = list(map(int,input().split()))
        #막대 어레이에 개미의 위치, ID 기록
        arr.append([p, a, a])
    while True:
        if len(arr) == 0:
            break
        arr = list(map(move, arr))
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                #같은 위치에 있을 시 충돌했다고 한다.
                if arr[i][0] == arr[j][0]:
                    crash(i, j)
        temp = []
        temp2 = []
        for n in range(len(arr)):
            if arr[n][0] < 0 or arr[n][0] > L:
                temp2.append(arr[n][2])
                temp.append(arr[n])
        for l in temp:
            arr.remove(l)
        if len(temp2) > 1:
            temp2 = sorted(temp2)
            fallenId = fallenId + temp2
        else:
            fallenId = fallenId + temp2        
        temp = []
        temp2 = []
    print(fallenId[k-1])


                    
