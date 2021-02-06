import sys

N, d, k, c = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr += arr[:k]
st = 0
end = k
S = arr[st:end]
maxVal = len(list(set(S + [c])))

while end < len(arr):
    st += 1
    end += 1
    S = arr[st:end]

    maxVal = max(maxVal, len(list(set(S + [c]))))
print(maxVal)
