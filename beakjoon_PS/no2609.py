def prime_list(n):
    #에라토스테네스의 체 초기화: n개 요소에 True설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True: #i가 소수인 경우
            for j in range(i+i, n, i): #i이후 i의 배수들을 False 판정
                sieve[j] = False
    #소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

N, M = map(int, input().split())

#자연수 N, M에 대해 소인수분해를 위해 소수 목록 구하기
N_prime = prime_list(N)
M_prime = prime_list(M)

#소인수 분해 결과 담기 위한 리스트
N_result = []
M_result = []
length = []
#N 소인수 분해하기
for i in N_prime:
    if N % i == 0:
        count = 0
        while N % i == 0:
            count += 1
            N = N//i
        N_result.append((i,count))
length.append(len(N_result))
#M 소인수 분해하기
for i in M_prime:
    if M % i == 0:
        count = 0
        while M % i == 0:
            count +=1
            M = M//i
        M_result.append((i,count))
length.append(len(M_result))
####
count2 = min(length)
#최대 공약수 구하기
Max_result = 1
for i in range(count2):
    if N_result[i][0] == M_result[i][0]:
        if N_result[i][1] <= M_result[i][1]:
            Max_result *= N_result[i][0]**N_result[i][1]
        else:
            Max_result *= N_result[i][0]**M_result[i][1]
print(Max_result)

#최소 공배수 구하기
lst =N_result + M_result
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i][0] == lst[j][0]:
            if lst[i][1] <= lst[j][1]:
                lst[i] = (1,1)
            else:
                lst[j] = (1,1)
Min_result = 1
for i in range(len(lst)):
    Min_result *= lst[i][0]**lst[i][1]
print(Min_result)