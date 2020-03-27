n = int(input())
stack = [0]
num = 0
arr_1 = []
arr_2 = []
for _ in range(n):
    _input = int(input())
    if stack[-1] < _input and _input not in arr_1:
        while stack[-1] < _input:
            num += 1
            if num not in arr_1:
                stack.append(num)
                arr_2.append("+")
        arr_1.append(stack.pop())
        arr_2.append("-")
    elif stack[-1] == _input and _input not in arr_1:
        arr_1.append(stack.pop())
        arr_2.append("-")
    elif stack[-1] > _input and _input not in arr_1:
        while stack[-1] > _input:
            arr_1.append(stack.pop())
            arr_2.append("-")
    else:
        arr_1.append("NO")
        break

if "NO" in arr_1:
    print("NO")
else:
    for i in arr_2:
        print(i)
