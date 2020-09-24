import sys
import collections
n = int(sys.stdin.readline())

stack = []
arr = collections.deque()
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
count = 1
temp = []
judge = True
while True:
    if len(arr) == 0:
        break
    if len(stack) == 0:
        stack.append(count)
        count += 1
        temp.append('+')
        continue
    if arr[0] > stack[-1]:
        stack.append(count)
        count += 1
        temp.append('+')
    elif arr[0] == stack[-1]:
        arr.popleft()
        stack.pop()
        temp.append('-')
    elif arr[0] < stack[-1]:
        judge = False
        break

if judge == False:
    print('NO')
else:
    for i in temp:
        print(i)
