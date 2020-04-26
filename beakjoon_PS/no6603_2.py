import sys
import itertools

while True:
    temp = sys.stdin.readline()
    if temp[0] == '0':
        break
    else:
        arr = list(map(int, temp.split()))
        k = arr.pop(0)
        arr = list(itertools.combinations(arr, 6))
        for element in arr:
            print(" ".join(map(str, element)))
        print("")
