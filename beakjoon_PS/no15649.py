### 백트래킹 함수
def backtracking(cnt,judge,seq):
    if cnt == M:
        return print(" ".join(map(str,seq)))
    
    for i in range(len(nums)):
        if judge[i] == 0:
            judge[i] = 1
            seq.append(nums[i])
            backtracking(cnt+1,judge,seq)
            seq.pop()
            judge[i] = 0
###입력
N, M = list(map(int,input().split()))

###1부터 N까지의 숫자리스트 선언
nums = [i for i in range(1,N+1)]

###숫자를 넣었는지 판단하는 judge 리스트 선언
judge = [0 for _ in range(1,N+1)]

###수열을 담을 리스트 선언
seq = []

###cnt선언
cnt = 0

###백트래킹 시작
backtracking(cnt,judge,seq)