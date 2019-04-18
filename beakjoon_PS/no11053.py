import sys

num = int(sys.stdin.readline())

D = [1 for i in range(num)]
arr = list(map(int,sys.stdin.readline().split()))

for i in range(num):
    D[i] =1
    for j in range(i, -1, -1):
        # print(j)
        if arr[j] < arr[i] and D[j] >= D[i]:
            D[i] = D[j] + 1
sys.stdout.write(str(max(D)))
