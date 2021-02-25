import sys


def bt(idx, res):
    global maxVal, minVal
    if idx == k+1:
        temp = "".join(res)
        if int(maxVal) < int(temp):
            maxVal = temp
        if int(minVal) > int(temp):
            minVal = temp
        return

    for i in range(10):
        if check[i] == 0:
            if table[idx] == 'any':
                res.append(str(i))
                check[i] = 1
                bt(idx + 1, res)
                check[i] = 0
                res.pop()
            elif table[idx] == 'up':
                if i > int(res[-1]):
                    res.append(str(i))
                    check[i] = 1
                    bt(idx + 1, res)
                    check[i] = 0
                    res.pop()
            elif table[idx] == 'down':
                if i < int(res[-1]):
                    res.append(str(i))
                    check[i] = 1
                    bt(idx+1, res)
                    check[i] = 0
                    res.pop()


k = int(sys.stdin.readline())
sign = [0] + sys.stdin.readline().split()
table = [0] * (k+1)
table[0] = 'any'
maxVal = -sys.maxsize
minVal = sys.maxsize
check = [0]*(10)
for i in range(1, len(sign)):
    if sign[i] == '<':
        table[i] = 'up'
    elif sign[i] == '>':
        table[i] = 'down'

bt(0, [])
print(maxVal)
print(minVal)
