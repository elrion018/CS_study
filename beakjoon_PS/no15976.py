import sys


def cal_xcorr(t):
    result = 0
    for i in range(N):
        for j in range(M):
            if (Y[j][0]+t)-X[i][0] == t:
                print("call")
                if X[i][0] >= 0 and Y[j][0] + t >= 0 and X[i][0] < X[-1][0]+1 and Y[j][0] + t < Y[-1][0] + 1:
                    result += X[i][1]*Y[j][1]
                    # print(result)
    return result


N = int(sys.stdin.readline())
X = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    X.append([temp[0], temp[1]])

M = int(sys.stdin.readline())
Y = []

for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    Y.append([temp[0], temp[1]])

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

ans = 0
# print(X[-1][0])
# print(Y[-1][0])
for t in range(a, b+1):
    ans += cal_xcorr(t)

print(ans)
