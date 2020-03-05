nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
N = int(input())
array = []
for _ in range(N):
    command = input()
    nums_sum = 0
    for i in list(command):
        if i in nums:
            nums_sum += int(i)
    array.append([command, nums_sum])
array.sort(key=lambda element: (len(element[0]), element[1], element[0]))

for element in array:
    print(element[0])
