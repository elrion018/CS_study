# 입력
goal = int(input())

sticks = [64]

# 반복

while True:
    sticks_sum = sum(sticks)
    if sticks_sum > goal:
        stick_min = min(sticks)
        sticks.pop(-1)
        sticks.append(stick_min/2)
        sticks.append(stick_min/2)
        temp = sum(sticks[0:-1])
        if temp >= goal:
            del(sticks[len(sticks)-1])
    else:
        break
print(len(sticks))
