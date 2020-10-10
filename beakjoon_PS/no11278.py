import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
result_num = 0
result_case = None
f = []
for _ in range(M):
    f.append(list(map(int, sys.stdin.readline().split())))

boolean = [False, True]

cases = list(itertools.product(boolean, repeat=N))

for case in cases:
    result = None
    for c in f:
        x1, x2 = c
        if x1 < 0 and x2 < 0:
            temp = (not case[abs(x1) - 1]
                    ) or (not case[abs(x2) - 1])
        elif x1 < 0:
            temp = (not case[abs(x1) - 1]) or case[x2-1]
        elif x2 < 0:
            temp = case[x1-1] or (not case[abs(x2) - 1])

        else:
            temp = case[x1-1] or case[x2-1]
        if result == None:
            result = temp
        else:
            result = result and temp
    if result == True:
        print(case)
        temp2 = []
        for element in case:
            if element == True:
                temp2.append('1')
            else:
                temp2.append('0')

        result_case = temp2
        result_num = 1
        break

if result_num == 1:
    print(result_num)
    print(" ".join(result_case))
else:
    print(0)
