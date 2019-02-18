class Queue:
    def __init__(self):
        self.Queue_item = []
    
    def push(self, x):
        self.Queue_item.append(x)
    
    def pop(self):
        judge = len(self.Queue_item)
        if judge < 1:
            return -1
        result = self.Queue_item[0]
        del self.Queue_item[0]
        return result

    def size(self):
        result = len(self.Queue_item)
        return result
    
    def empty(self):
        result = len(self.Queue_item)
        if result < 1:
            return 1
        else:
            return 0
    
    def front(self):
        result = len(self.Queue_item)
        if result < 1:
            return -1
        else:
            return self.Queue_item[0]

    def back(self):
        result = len(self.Queue_item)
        if result < 1:
            return -1
        else:
            return self.Queue_item[-1]

Q = Queue()
N = int(input())
for _ in range(N):
    cmd = list(input().split(' '))
    if cmd[0] == 'push':
        Q.push(cmd[1])
    elif cmd[0] == 'pop':
        print(Q.pop())
    elif cmd[0] == 'size':
        print(Q.size())
    elif cmd[0] == 'empty':
        print(Q.empty())
    elif cmd[0] == 'front':
        print(Q.front())
    elif cmd[0] == 'back':
        print(Q.back())




        