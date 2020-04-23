import sys
sys.setrecursionlimit(100000)


def backTracking(k, arr, count, result):
    if count == 6:
        return print(" ".join(map(str, result)))

    for i in range(k-count):
        if len(result) == 0:
            temp = arr.pop(i)
            result.append(temp)
            backTracking(k, arr, count+1, result)
            result.pop()
            arr.insert(i, temp)
        else:
            if result[-1] < arr[i]:
                temp = arr.pop(i)
                result.append(temp)
                backTracking(k, arr, count+1, result)
                result.pop()
                arr.insert(i, temp)


while True:
    temp = sys.stdin.readline()
    if temp[0] == '0':
        break
    arr = list(map(int, temp.split()))
    k = arr.pop(0)
    count = 0
    backTracking(k, arr, count, [])
    print("")
