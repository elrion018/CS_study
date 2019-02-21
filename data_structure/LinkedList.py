class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
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
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next

        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    node.next = node.next.next

                else:
                    node = node.next
        

L = Linked_list(1)
L.add(2)
L.add(3)
L.add(4)
L.delete(3)
L.desc()
