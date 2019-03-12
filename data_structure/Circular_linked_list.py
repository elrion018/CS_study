class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self,data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            if node.data < data:
                node.next = Node(data)
            else:
                node = self.head
                while node.next.data < data:
                    node = node.next
                temp = node.next
                new = Node(data)
                new.next = temp
                node.next = new
                del temp

    def desc(self):
        node = self.head
        while True:
            print(node.data)
            if node.next is None:
                node = self.head
            else:
                node = node.next
    
    def delete(self, data):
        if self.head == '':
            print('해당 값을 가진 노드가 없습니다')
            return False
        if self.head.data == data:
            
            self.head = self.head.next
            
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    
                    node.next = node.next.next
                    
                else:
                    node = node.next
            
C = NodeMgmt(0)
C.add(1)
C.add(2)
C.add(3)
C.add(4)
C.add(5)
C.desc()

            

