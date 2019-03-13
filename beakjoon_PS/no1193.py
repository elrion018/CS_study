X = int(input())
num = 0
plus = 0
lst = []
while num < X:
    plus += 1
    num = num + plus
    for i in range(plus):
        if plus % 2 == 1:
            lst.append('%d/%d' % (plus-i ,i+1))

        elif plus % 2 == 0:
            lst.append('%d/%d' % (i+1, plus-i))
print(lst[X-1])

