import sys
arr = list(sys.stdin.readline())[:-1]
acc = 0
result = 0
nums = []
for i in reversed(range(len(arr))):

    if i == 0:
        nums.append(arr[i])
        temp = ''
        for i in reversed(nums):
            temp += i
        acc += int(temp)
        result += acc
    elif arr[i] == '-':
        temp = ''
        for i in reversed(nums):
            temp += i
        acc += int(temp)
        result -= acc
        acc = 0
        nums = []
    elif arr[i] == '+':
        temp = ''
        for i in reversed(nums):
            temp += i
        acc += int(temp)
        nums = []
    elif arr[i] != '-' and arr[i] != '+':
        nums.append(arr[i])
print(result)
