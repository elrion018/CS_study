

def push(x):
    return stack.append(x)


def pop():
    if len(stack) == 0:
        return print(-1)
    else:
        return print(stack.pop())


def size():
    return print(len(stack))


def empty():
    if len(stack) == 0:
        return print(1)
    else:
        return print(0)


def top():
    if len(stack) == 0:
        return print(-1)
    else:
        return print(stack[-1])


# 입력
stack = []
N = int(input())
for _ in range(N):
    temp = list(input().split())

    if temp[0] == 'push':
        push(int(temp[1]))

    elif temp[0] == 'top':
        top()

    elif temp[0] == 'size':
        size()

    elif temp[0] == 'empty':
        empty()
    elif temp[0] == 'pop':
        pop()
