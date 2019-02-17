T = int(input())

for _ in range(T):
    stack = []
    judge = 'T'
    VPS = list(input())
    for i in range(len(VPS)):
        if VPS[i] == '(':
            stack.append(1)
        elif VPS[i] == ')':
            if len(stack) == 0:
                judge = 'F'
                break
            else:
                stack.pop()
    if len(stack) != 0:
        judge = 'F'
    if judge == 'T':
        print('YES')
    else:
        print('NO')
                