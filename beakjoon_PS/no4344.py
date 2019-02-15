
t_c = int(input())
cases = []
for i in range(t_c): #for 문의 i는 꼭 사용하지 않아도 된다.
    #map의 결과물은 리스트가 아니므로 리스트를 씌워줘야함.
    #입력 후 연속된 입력은 for 문을 통해서 나타낼 수 있음.
    cases.append(list(map(int,input().split())))

for case in cases:
    cnt = 0
    mean = sum(case[1:])/(len(case)-1)
    for j in range(1,case[0]+1):
        if case[j] > mean:
            cnt+=1 #자동적으로 변수를 증가 시킬 때 =+을 유용하게 쓰자
    ratio = round(cnt/case[0],6) #반올림하는 round함수 반올림하는 자릿수도 지정할 수 있음.
    print('%.3f' % (ratio*100) + '%') # % 포멧팅을 사용. 그리고 원하는 소수점 까지 .3f 등의 방법으로 나타낼 수 있음.
        

    


