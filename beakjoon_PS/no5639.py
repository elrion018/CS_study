class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = Node(None)
        self.postorder_list = []
        self.judge_list = []
    
    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)


    def __add_node(self, cur, item):
        if cur.val > item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        elif cur.val < item:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)
    
    def postorder_traverse(self): 
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)
bt = BinaryTree()
inputs = []
while True:
    inp = input()
    if inp == "":
        break
    bt.add(inp)
bt.postorder_traverse()
for i in bt.postorder_list:
    print(i)