import sys

t = int(sys.stdin.readline())

for t in range(t):
    d = [0, 0, 0, 0]
    s = list(sys.stdin.readline().strip())
    string = ""
    for i in s:
        if i == 'L':
            d[0] += 1
        elif i == 'R':
            d[1] += 1
        elif i == 'U':
            d[2] += 1
        elif i == 'D':
            d[3] += 1
    if d[0] > 0 and d[1] > 0 and d[2] > 0 and d[3] > 0:
        minVal1 = min(d[0:2])
        minVal2 = min(d[2:4])
        for i in range(0, 2):
            d[i] = minVal1
        for i in range(2, 4):
            d[i] = minVal2
        temp = d[1]
        d[1] = d[2]
        d[2] = temp
        for j in range(len(d)):
            if j == 0:
                string += 'L'*d[j]
            elif j == 1:
                string += 'U'*d[j]
            elif j == 2:
                string += 'R'*d[j]
            elif j == 3:
                string += 'D'*d[j]
        print(len(string))
        print(string)
    elif (d[0] > 0 and d[1] > 0 and d[2] == 0 and d[3] == 0):  # L R U D
        print(2)
        print("LR")
    elif (d[0] > 0 and d[1] > 0 and d[2] > 0 and d[3] == 0):
        print(2)
        print("LR")
    elif (d[0] > 0 and d[1] > 0 and d[2] == 0 and d[3] > 0):
        print(2)
        print("LR")
    elif (d[0] == 0 and d[1] == 0 and d[2] > 0 and d[3] > 0):
        print(2)
        print("UD")
    elif (d[0] == 0 and d[1] > 0 and d[2] > 0 and d[3] > 0):
        print(2)
        print("UD")
    elif (d[0] > 0 and d[1] == 0 and d[2] > 0 and d[3] > 0):
        print(2)
        print("UD")

    else:
        print(0)
