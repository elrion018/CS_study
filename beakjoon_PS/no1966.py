T = int(input())
for _ in range(T):
    NM = list(map(int,input().split(' ')))
    N = NM[0]
    M = NM[1]
    imp = list(map(int,input().split(' ')))
    judge = [0 for _ in range(N)]
    judge[M] = 'T'
    cnt = 0
    if len(imp) == N:
        while True:
            if imp[0] == max(imp):
                cnt += 1
                if judge[0] == 'T':
                    print(cnt)
                    break
                else:
                    imp.pop(0)
                    judge.pop(0)
            else:
                imp.append(imp.pop(0))
                judge.append(judge.pop(0))




    