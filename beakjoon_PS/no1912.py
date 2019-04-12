import sys
n = list(map(int, sys.stdin.readline().split()))
nums = list(map(int,sys.stdin.readline().split()))
numsSum = 0
sumList = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        numsSum = 0
        for k in range(i, j+1):
            numsSum += nums[k]
        sumList.append(numsSum)

sumList = list(set(sumList))
print(max(sumList))