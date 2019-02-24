#순환큐 구현

class circular_Queue:
    def __init__(self, max):
        self.max = max
        self.list = [None] * self.max
        self.size = self.rear = self.front = 0

    def next_idx(self, idx):
        return (idx + 1) % self.max
    
    def enqueue(self, item):
        if self.next_idx(self.rear) == self.front:
            print('큐가 꽉 찼습니다')
        else:
            self.rear = self.next_idx(self.rear)
            self.list[self.rear] = item
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print('큐가 비었습니다')
        else:
            self.front = self.next_idx(self.front)
            self.list[self.front] = None
            self.size -= 1

    def peek(self):
        self.front = self.next_idx(self.front)
        print(self.list[self.front])

    def display(self):
        current = self.front
        while current != self.rear:
            current = self.next_idx(current)
            print(self.list[current])

        