import sys

N = int(sys.stdin.readline())
temp = ""
count = 0
for _ in range(2*N-1):
    if count < N:
        temp += "*"
        print(temp)
        count += 1
    else:
        temp = temp[:-1]
        print(temp)
