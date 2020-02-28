N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

array.sort(key=lambda element: (element[0], element[1]))

for [i, j] in array:
    print(i, j)
