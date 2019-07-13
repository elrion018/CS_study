#X입력
X = int(input())

#막대 어레이
arr = [64]

while True:
    if sum(arr) > X:
        Min = arr[-1]
        arr = arr[0:-1]
        arr.append(Min//2)
        arr.append(Min//2)
        if sum(arr[0:-1]) >= X:
            arr = arr[0:-1]
    else:
        print(len(arr))
        break
