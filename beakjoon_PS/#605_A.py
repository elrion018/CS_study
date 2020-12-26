import sys

t = int(sys.stdin.readline())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    nums = sorted(nums)
    mid = nums[1]

    judge1 = True
    same = []
    for i in range(len(nums)):
        if mid != nums[i]:
            judge1 = False
        else:
            same.append(i)

    if judge1 == True:
        print("0")
    else:
        for i in range(len(nums)):
            if mid == nums[i]:
                pass
            elif mid > nums[i]:
                nums[i] += 1
            elif mid < nums[i]:
                nums[i] -= 1
        if same == [0, 1] and nums[1] < nums[2]:
            nums[0] += 1
            nums[1] += 1
        elif same == [1, 2] and nums[1] > nums[0]:
            nums[1] -= 1
            nums[2] -= 1
        print(abs(nums[0]-nums[1]) +
              abs(nums[0] - nums[2]) + abs(nums[1] - nums[2]))
