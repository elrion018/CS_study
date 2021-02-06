import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

S = 0

st = 0
end = 0
cnt = 0

while st < N:

    if S >= M or end == N:
        st += 1
        S -= arr[st-1]
    elif S < M:
        end += 1
        S += arr[end-1]
    if S == M:
        cnt += 1
print(cnt)
