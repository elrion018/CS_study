count = 0
date = input()
cars = input().split()
for car in cars:
    if date in car:
        count += 1
print(count)
