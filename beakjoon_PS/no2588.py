import sys
one = sys.stdin.readline()
two = sys.stdin.readline()
three = int(one) * int(two[2])
four = int(one) * int(two[1])
five = int(one) * int(two[0])
print(three)
print(four)
print(five)
print(three+(four*10)+(five*100))