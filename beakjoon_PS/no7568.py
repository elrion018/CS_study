import sys

N = int(sys.stdin.readline())
mans = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    rank = 1
    for j in range(N):
        if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1]:
            rank += 1
    print(rank, end=" ")
