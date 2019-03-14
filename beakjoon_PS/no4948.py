def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True]*(2*n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int((2*n+1)**0.5)
    for i in range(2, m+1):
        if sieve[i] == True: #i가 소수인 경우
            for j in range(i+i,2*n+1,i):
                sieve[j] = False
    #소수 목록 산출
    return len([i for i in range(n+1,2*n+1) if sieve[i] == True])

while True:
    n = int(input())
    if n == 0:
        break
    print(prime_list(n))
