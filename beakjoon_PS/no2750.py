N = int(input())
result = []
if N >= 1 and N<= 1000:
    for _ in range(N):
        num = int(input())
        if num not in result:
            result.append(num)
        else:
            break
result.sort()
for i in result:
    print(i)
        
