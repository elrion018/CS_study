import sys

N, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

st = 0
end = K

maxVal = sum(arr[st:end])
S = sum(arr[st:end])

while end < N:
    st += 1
    end += 1
    S -= arr[st-1]
    S += arr[end-1]

    maxVal = max(maxVal, S)
print(maxVal)
