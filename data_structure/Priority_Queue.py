#노드 클래스 생성
class Node:
    def __init__(self, data, pri):
        self.data = data
        self.next = None
        self.pri = pri

#우선순위 큐
#링크드 큐이기도 함
class Priority_Queue:
    def __init__(self, data, pri):
        self.head = Node(data, pri)

    def Enqueue(self,data, pri):
        node = self.head
        while node.next:
            node = node.next
        if node.pri < pri:
            node.next = Node(data,pri)
        else: #node.pri >= pri
            node = self.head
            while node.next.pri < pri:
                node = node.next
            temp = node.next
            new = Node(data, pri)
            new.next = temp
            node.next = new
            del new

    def Dequeue(self):
        node = self.head
        while node.next:
            if node.next.next is None:
                node.next = None
                break
            else:
                node = node.next

    def display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next






            













