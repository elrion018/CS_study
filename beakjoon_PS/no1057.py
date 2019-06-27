#입력
N, kim, im = list(map(int,input().split(' ')))

#라운드 셀 count 변수 선언
count = 0

#배열 생성
arr = [0 for i in range(N)]

#김지민, 임한수 배치
arr[kim-1] = 1
arr[im-1] = 1

#판단하는 변수 선언
judge = 0

#대전 붙이기
while judge != 1:
    #임시 배열 선언
    temp = []
    for i in range(0, len(arr), 2):

        #마지막 대진에서 대전 상대가 존재하는지 안하는지 부터 판별
        if i == len(arr)-1 and arr[i] == 1: 
            temp.append(1)
        elif i == len(arr)-1 and arr[i] == 0:
            temp.append(0)

        else:
            #김지민이랑 임한수끼리 붙었을 때
            if arr[i] == 1 and arr[i+1] == 1:
                judge += 1
            #김지민과 임한수가 서로가 아닌 다른 사람이랑 붙었을때
            elif arr[i] == 1 or arr[i+1] == 1:
                temp.append(1)
            #김지민과 임한수가 아닌 사람들끼리 붙었을 때
            else:
                temp.append(0)
                
    arr = temp
    count += 1

print(count)
    

