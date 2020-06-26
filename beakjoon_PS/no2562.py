import sys
arr = []
for _ in range(9):
    arr.append(int(sys.stdin.readline()))
maxVal = [-sys.maxsize, 99]

for i in range(9):
    if maxVal[0] < arr[i]:
        maxVal = [arr[i], i+1]
for j in maxVal:
    print(j)
