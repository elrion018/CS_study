# nums = list(map(int,list(input().split(' '))))
# first_num = 100*(nums[0] % 10) + ((nums[0] % 100) - (nums[0] % 10)) + (nums[0] // 100)
# second_num = 100*(nums[1] % 10) + ((nums[1] % 100) - (nums[1] % 10)) + (nums[1] // 100)
# if first_num > second_num:
#     print(first_num)
# else:
#     print(second_num)
print(max(input()[::-1].split()))