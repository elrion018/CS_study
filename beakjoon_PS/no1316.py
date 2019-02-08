def check(voca):
    for i in range(len(voca)):
        judge = ['F','F']
        for j in range(i+1,len(voca)):
            if voca[i] != voca[j]:
                judge[0] = 'T'
            if voca[i] == voca[j] and judge[0] == 'T':
                judge[1] = 'T'
            if judge[0] == 'T' and judge[1] == 'T':
                return 0
    return 1
N = int(input())
cnt = 0
for k in range(N):
    cnt += check(input())
print(cnt)
    