import sys
minVal = 1000000000
maxVal = -1000000000
result = []


def backTracking(seq, operators, op):
    global minVal
    global maxVal
    global result
    if len(operators) == 0:
        calVal = seq[0]
        for i in range(len(op)):
            if op[i] == '+':
                calVal += seq[i+1]
            elif op[i] == '-':
                calVal -= seq[i+1]
            elif op[i] == '*':
                calVal *= seq[i+1]
            elif op[i] == '/':
                if calVal >= 0:
                    calVal = calVal // seq[i+1]
                else:
                    calVal = -(abs(calVal) // 2)
        if minVal > calVal:
            minVal = calVal
        if maxVal < calVal:
            maxVal = calVal
        result.append(calVal)
        return
    for i in range(len(operators)):
        temp_2 = operators.pop(i)
        op.append(temp_2)
        backTracking(seq, operators, op)
        op.pop()
        operators.insert(i, temp_2)


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
temp = list(map(int, sys.stdin.readline().split()))
operators = []
op = []

for i in range(4):
    for _ in range(temp[i]):
        if i == 0:
            operators.append('+')
        elif i == 1:
            operators.append('-')
        elif i == 2:
            operators.append('*')
        elif i == 3:
            operators.append('/')
backTracking(seq, operators, op)
print(maxVal)
print(minVal)
