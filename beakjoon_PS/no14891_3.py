import collections


def run():
    for turn in turns:
        left_turn(turn[0]-1, -turn[1])
        right_turn(turn[0]+1, -turn[1])
        gears[turn[0]].rotate(turn[1])

    return cal()


def left_turn(num, d):
    if num < 0:
        return

    if gears[num][2] != gears[num+1][6]:
        left_turn(num-1, -d)
        gears[num].rotate(d)


def right_turn(num, d):
    if num > 3:
        return
    if gears[num][6] != gears[num-1][2]:
        right_turn(num+1, -d)
        gears[num].rotate(d)


def cal():
    result = 0
    for i in range(4):
        if gears[i][0] == 1:
            result += 2**i
    return result


gears = []
turns = []

for _ in range(4):

    gears.append(collections.deque(list(map(int, input()))))

K = int(input())

for _ in range(K):
    v1, v2 = map(int, input().split())
    turns.append([v1-1, v2])


print(run())
