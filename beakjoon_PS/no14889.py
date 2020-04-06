import sys
import itertools


def team(member):
    allMember = [i for i in range(N)]
    start_team = []
    link_team = []

    # 맴버 선택
    for i in allMember:
        if i in member:
            start_team.append(i)
        else:
            link_team.append(i)
    start_sum = 0
    for i in start_team:
        for j in start_team:
            start_sum += arr[i][j]

    link_sum = 0
    for i in link_team:
        for j in link_team:
            link_sum += arr[i][j]

    return abs(start_sum - link_sum)


def solve(members):
    # 모든 경우의 수 뽑기
    combination_members = itertools.combinations(members, int(N/2))
    selected_members = list(combination_members)
    length = int(len(selected_members)/2)

    minVal = sys.maxsize
    for member in selected_members[:length]:
        minus = team(member)

        if minVal > minus:
            minVal = minus

    print(minVal)


N = int(sys.stdin.readline())
members = [i for i in range(N)]

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

solve(members)
