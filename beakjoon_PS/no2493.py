import sys
N = int(sys.stdin.readline())
tower = [0] + list(map(int, sys.stdin.readline().split()))
stack = []
for i in range(1, N+1):

    while stack:
        if tower[i] > stack[-1][0]:
            stack.pop()

        else:
            break

    if not stack:
        print(0, end=' ')

    else:
        print(stack[-1][1], end=' ')

    stack.append((tower[i], i))
