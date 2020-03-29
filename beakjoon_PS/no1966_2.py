t = int(input())
for _ in range(t):
    count = 0
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    judge = [False for _ in range(N)]
    judge[M] = True
    while docs:
        if docs[0] == max(docs):
            count += 1
            if judge[0] == True:
                print(count)
                docs.pop(0)
                judge.pop(0)
            else:
                docs.pop(0)
                judge.pop(0)
        else:
            docs.append(docs.pop(0))
            judge.append(judge.pop(0))
