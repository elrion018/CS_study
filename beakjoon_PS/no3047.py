

nums = list(map(int, input().split()))
orders = list(input())

nums = sorted(nums)
A = nums[0]
B = nums[1]
C = nums[2]

for order in orders:
    if order == 'A':
        print(A, end=' ')
    elif order == 'B':
        print(B, end=' ')
    elif order == 'C':
        print(C, end=' ')
