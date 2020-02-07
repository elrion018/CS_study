N = input()
result = 0
length = len(N)
for i in range(1, length):
    result += i*(9*(10**(i-1)))
left = int(N) - 10**(length-1)
result += length * (left+1)
print(result)
