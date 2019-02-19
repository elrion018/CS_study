class deque:
    def __init__(self):
        self.items = []
    def push_front(self,x):
        self.items.insert(0,x)
    def pop_front(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop(0)
    def push_back(self,x):
        self.items.append(x)
    def pop_back(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[0]
    def back(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]

D = deque()
N = int(input())
for _ in range(N):
    cmd = list(input().split(' '))
    if cmd[0] == 'push_back':
        D.push_back(int(cmd[1]))
    elif cmd[0] == 'push_front':
        D.push_front(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        print(D.pop_front())
    elif cmd[0] == 'pop_back':
        print(D.pop_back())
    elif cmd[0] == 'size':
        print(D.size())
    elif cmd[0] == 'empty':
        print(D.empty())
    elif cmd[0] == 'front':
        print(D.front())
    elif cmd[0] == 'back':
        print(D.back())
