stack = []
judge = True
while True:
    strings = input()
    if strings == ".":
        break
    else:
        for i in list(strings):
            if i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) != 0:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        judge = False
                else:
                    judge = False
            elif i == '[':
                stack.append(i)

            elif i == ']':
                if len(stack) != 0:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        judge = False
                else:
                    judge = False
        if len(stack) == 0 and judge:
            judge = True
            print("yes")

        else:
            judge = True
            stack = []
            print("no")
