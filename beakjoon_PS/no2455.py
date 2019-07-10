count = 0
arr = []
for _ in range(4):
    Out, In = list(map(int,input().split()))
    count = count - Out + In
    arr.append(count)

print(max(arr))

