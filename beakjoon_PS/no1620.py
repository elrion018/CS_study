N, M = map(int,input().split())
mydict = dict()
mydict2 = dict()
key = 0
for _ in range(1,N+1):
    mon = input()
    key += 1
    mydict[key] = mon
    mydict2[mon] = key

for _ in range(M):
    question = input()
    if question.isdigit() is True:
        print(mydict[int(question)])
        
    else:
        print(mydict2[question])
