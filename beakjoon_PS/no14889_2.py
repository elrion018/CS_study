import sys


def bs(N, mans, count, start_team, link_team, S):
    global minVal
    if count == mans:
        start_sum = 0
        for i in start_team:
            for j in start_team:
                if i != j:
                    start_sum += S[i][j]
        link_sum = 0
        for i in link_team:
            for j in link_team:
                if i != j:
                    link_sum += S[i][j]
        diff = abs(start_sum - link_sum)

        if minVal > diff:
            minVal = diff
        return
    for i in range((N-count)):
        temp = link_team.pop(i)
        start_team.append(temp)
        bs(N, mans, count+1, start_team, link_team, S)
        start_team.pop()
        link_team.insert(i, temp)


N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
link_team = [i for i in range(N)]
start_team = []
count = 0
minVal = sys.maxsize
bs(N, N//2, count, start_team, link_team, S)
print(minVal)
