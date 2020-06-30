import sys


burgers = []
drinks = []
results = []
for i in range(5):
    if i < 3:
        burgers.append(int(sys.stdin.readline()))
    else:
        drinks.append(int(sys.stdin.readline()))

for burger in burgers:
    for drink in drinks:
        results.append(burger+drink-50)
print(min(results))
