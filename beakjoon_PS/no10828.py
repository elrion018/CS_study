class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items == []:
            return -1
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def empty(self):
        if self.items == []:
            return 1
        else:
            return 0
    def top(self):
        if self.items == []:
            return -1
        else:
            return self.items[-1]
stk = stack()
N = int(input())
for _ in range(N):
    cmd = input().split(' ')
    if cmd[0] == 'push':
        stk.push(cmd[1])
    elif cmd[0] == 'pop':
        print(stk.pop())
    elif cmd[0] == 'size':
        print(stk.size())
    elif cmd[0] == 'empty':
        print(stk.empty())
    elif cmd[0] == 'top':
        print(stk.top())