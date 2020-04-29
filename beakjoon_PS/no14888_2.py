import sys
import itertools

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
op_count = list(map(int, sys.stdin.readline().split()))
operators = ['+', '-', '*', '/']
operators_list = []
minVal = sys.maxsize
maxVal = -sys.maxsize
for i in range(4):
    operators_list.extend(operators[i]*op_count[i])

result = set(list(itertools.permutations(operators_list, N-1)))

for element in result:
    calVal = seq[0]
    for i in range(N-1):
        if element[i] == '/':
            if calVal > 0:
                calVal = calVal // seq[i+1]
            else:
                calVal = -(abs(calVal) // seq[i+1])
        else:
            if element[i] == '+':
                calVal += seq[i+1]
            elif element[i] == '-':
                calVal -= seq[i+1]
            elif element[i] == '*':
                calVal *= seq[i+1]
    if minVal > calVal:
        minVal = calVal
    if maxVal < calVal:
        maxVal = calVal

print(maxVal)
print(minVal)
