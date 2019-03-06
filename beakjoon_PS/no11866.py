N, M = map(int,input().split())
lst = [i for i in range(1,N+1)]
result = []

while lst:
        count = 0
        while True:
                count += 1
                temp = lst[0]
                lst = lst[1:]
                lst = lst + [temp]

                if count == M-1:
                        result = result + [str(lst.pop(0))]
                        break

result2 = ', '.join(result)
print('<%s>' % result2)