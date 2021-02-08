import sys

N, d, k, c = map(int, sys.stdin.readline().split())

table = [0]*(d+1)
table[c] = 1
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr += arr[:k]
st = 0
end = k
maxVal = 1
for i in range(st, end):
    table[arr[i]] += 1
    if table[arr[i]] < 2:
        maxVal += 1
temp = maxVal
while end < len(arr):
    table[arr[st]] -= 1
    if table[arr[st]] < 1:
        temp -= 1
    st += 1
    table[arr[end]] += 1
    if table[arr[end]] < 2:
        temp += 1
    end += 1
    maxVal = max(maxVal, temp)
print(maxVal)
