
###백트래킹 함수
def backtracking(cnt,mList):
    if cnt == M:
        print(' '.join(map(str,mList)))
        return
    for i in range(len(nums)):
        if len(mList) == 0:
            mList.append(nums[i])
            backtracking(cnt+1,mList)
            mList.pop()
        elif nums[i] >= mList[-1]:
            mList.append(nums[i])
            backtracking(cnt+1,mList)
            mList.pop()


###입력
N, M = list(map(int, input().split()))

### 1부터 N 까지 자연수 리스트 선언
nums = [i for i in range(1,N+1)]

###백트래킹
backtracking(0,[])