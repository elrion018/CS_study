class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def pop(self):
        if self.head is None:
            print("pop할 리스트가 없습니다.")
        else:
            cur = self.head
            prev = None
            while cur.next is not None:
                prev = cur
                cur = cur.next
            prev.next = None

    def getAllValues(self):
        if self.head is None:
            print("리스트 안에 노드가 없습니다.")
        else:
            cur = self.head
            while cur.next != None:
                print(cur.value)
                cur = cur.next
            print(cur.value)

    def getValueIndex(self, value):
        idx = 0
        if self.head.value == value:
            print(idx)
        else:
            cur = self.head
            while cur.value != value and cur.next != None:
                idx += 1
                cur = cur.next

            if cur.value == value:
                print(idx)
            else:
                print("해당 인덱스엔 노드가 없습니다.")

    def insertNodeAtIndex(self, targetIdx, node):
        idx = 0
        prev = None
        cur = self.head
        while idx != targetIdx and cur.next != None:
            idx += 1
            prev = cur
            cur = cur.next
        if idx == targetIdx:
            if prev is None:
                self.head = node
                self.head.next = cur
            else:
                node.next = cur
                prev.next = node
        else:
            print("해당 인덱스에 노드를 삽입할 수 없습니다.")

    def deleteNodeAtIndex(self, targetIdx):
        idx = 0
        prev = None
        cur = self.head
        while idx != targetIdx and cur.next != None:
            idx += 1
            prev = cur
            cur = cur.next
        if idx == targetIdx:
            if prev is None:
                self.head = cur.next
            else:
                prev.next = cur.next
        else:
            print("해당 인덱스에 노드를 제거할 수 없습니다.")

    def clear(self):
        self.head = None


link = singlyLinkedList()

for i in range(3):
    link.append(Node(i))


link.clear()
link.getAllValues()
