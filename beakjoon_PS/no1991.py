           
#이진트리구성하기
class Node:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

class binary_tree:
    def __init__(self):
        self.root = None
        self.preorder = []
        self.inorder = []
        self.postorder =[]

    def add(self, data):
        if self.root is None:
            self.root = Node(data[0])
            self.root.leftchild = Node(data[1])
            self.root.rightchild = Node(data[2])
        else:
            self.__add(self.root.leftchild, data)
            self.__add(self.root.rightchild, data)
            
    def __add(self,cur,data):
        if cur is None:
            pass
        else:
            if cur.data == data[0]:
                cur.leftchild = Node(data[1])
                cur.rightchild = Node(data[2])
            else:
                self.__add(cur.leftchild, data)
                self.__add(cur.rightchild, data)

    def PreOrder(self):
        if self.root is not None:
            self.__pre(self.root)

    def __pre(self, cur):
        self.preorder.append(cur.data)
        if cur.leftchild is not None:
            self.__pre(cur.leftchild)
        if cur.rightchild is not None:
            self.__pre(cur.rightchild)
    
    def InOrder(self):
        if self.root is not None:
            self.__in(self.root)
    
    def __in(self, cur):
        if cur.leftchild is not None:
            self.__in(cur.leftchild)
        self.inorder.append(cur.data)
        if cur.rightchild is not None:
            self.__in(cur.rightchild)

    def PostOrder(self):
        if self.root is not None:
            self.__post(self.root)
    
    def __post(self, cur):
        if cur.leftchild is not None:
            self.__post(cur.leftchild)
        if cur.rightchild is not None:
            self.__post(cur.rightchild)
        self.postorder.append(cur.data)

B = binary_tree()

num = int(input())
for i in range(num):
    in_put = input().split(' ')
    B.add(in_put)

B.PreOrder()
B.InOrder()
B.PostOrder()
result = [B.preorder, B.inorder, B.postorder]
for i in result:
    while '.' in i:
        i.remove('.')
print(''.join(B.preorder))
print(''.join(B.inorder))
print(''.join(B.postorder))