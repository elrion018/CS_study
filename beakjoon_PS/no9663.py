import sys
sys.setrecursionlimit(10**6)
result = 0


def backTracking(N, issued1, issued2, issued3, y, count):
    global result
    if count == N:
        result += 1
        return

    for x in range(N):
        if issued1[x] == False and issued2[y+x] == False and issued3[y-x+N-1] == False:
            issued1[x] = True
            issued2[y+x] = True
            issued3[y-x+N-1] = True
            backTracking(N, issued1, issued2, issued3, y+1, count+1)
            issued1[x] = False
            issued2[y+x] = False
            issued3[y-x+N-1] = False


N = int(sys.stdin.readline())
issued1 = [False] * N
issued2 = [False] * (2*N - 1)
issued3 = [False] * (2*N - 1)
backTracking(N, issued1, issued2, issued3, 0, 0)
print(result)
