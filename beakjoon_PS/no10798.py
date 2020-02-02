length = 0
voca = []
for _ in range(5):
    temp = list(input())
    voca.append(temp)
    if len(temp) > length:
        length = len(temp)
for i in range(length):
    for j in range(5):
        if i < len(voca[j]):
            print(voca[j][i], end='')
