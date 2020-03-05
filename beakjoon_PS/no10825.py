N = int(input())

scores = [input().split() for _ in range(N)]

scores.sort(
    key=lambda element: (-int(element[1]), int(element[2]), -int(element[3]), element[0]))

for element in scores:
    print(element[0])
