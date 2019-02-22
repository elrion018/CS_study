num = input()
count = int(num)
nums = list(map(int,input().split(' ')))
if len(nums) == int(num):
    for i in nums:
        if i != 1:
            for j in range(2,i):
                if (i/j) % 1 == 0:
                    count -=1
                    break
        else:
            count -=1
else:
    pass
print(count)
