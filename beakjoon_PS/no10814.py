N = int(input())
array = [list(input().split()) + [i] for i in range(N)]
array.sort(key=lambda element: (int(element[0]), element[2]))
for element in array:
    print(element[0], element[1])
