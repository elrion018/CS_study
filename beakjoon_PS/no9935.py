import sys

stack = []
string = list(sys.stdin.readline().strip())
es = list(sys.stdin.readline().strip())

for i in range(len(string)):
    stack.append(string[i])
    if len(string) >= len(es) and stack[-len(es):] == es:
        print("call")
        for _ in range(len(es)):
            stack.pop()
print(string)
