

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def size(self):
        if self.left:
            l = self.left.size()
        else:
            l = 0
        if self.right:
            r = self.right.size()
        else:
            r = 0
        return l + r + 1

    def depth(self):
        if self.left:
            ld = self.left.depth()
        else:
            ld = 0
        if self.right:
            rd = self.right.depth()
        else:
            rd = 0
        if ld > rd:
            return ld + 1
        else:
            return rd + 1


class Tree:
    def __init__(self):
        self.root = None
        return

    def preOrderTraverse(self):
        traversal = []

        def _preOrderTraverse(node):
            if node is None:
                pass
            else:
                traversal.append(node.value)
                _preOrderTraverse(node.left)
                _preOrderTraverse(node.right)
        _preOrderTraverse(self.root)
        print(traversal)

    def inOrderTraverse(self):
        traversal = []

        def _inOrderTraverse(node):
            if node is None:
                pass
            else:
                _inOrderTraverse(node.left)
                traversal.append(node.value)
                _inOrderTraverse(node.right)
        _inOrderTraverse(self.root)
        print(traversal)

    def postOrderTraverse(self):
        traversal = []

        def _postOrderTraverse(node):
            if node is None:
                pass
            else:
                _postOrderTraverse(node.left)
                _postOrderTraverse(node.right)
                traversal.append(node.value)
        _postOrderTraverse(self.root)
        print(traversal)

    def insertNode(self, node):
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            while True:
                if node.value > cur.value:
                    if cur.right == None:
                        cur.right = node
                        return
                    else:
                        cur = cur.right
                elif node.value < cur.value:
                    if cur.left == None:
                        cur.left = node
                        return
                    else:
                        cur = cur.left
                else:
                    print("이 노드는 이미 존재하고 있습니다.")
                    return

    def deleteNode(self, targetValue):

        def _deleteNode(node, targetValue):
            if node is None:
                print("삭제할 노드가 없습니다.")
                return

            if node.value == targetValue:
                if node.left and node.right:
                    parent = node
                    child = node.right
                    while child.left is not None:
                        parent = child
                        child = child.left
                    child.left = node.left
                    child.right = node.right
                    node = child

                elif node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                else:
                    node = None

            elif node.value > targetValue:
                node.left = _deleteNode(node.left, targetValue)
            else:
                node.right = _deleteNode(node.right, targetValue)
            return node
        self.root = _deleteNode(self.root, targetValue)

    def size(self):
        return self.root.size()

    def depth(self):
        return self.root.depth()


tree = Tree()


tree.insertNode(Node(1))
tree.insertNode(Node(4))
tree.insertNode(Node(3))
tree.insertNode(Node(6))
tree.insertNode(Node(7))
tree.insertNode(Node(2))
tree.insertNode(Node(5))
tree.insertNode(Node(8))
tree.insertNode(Node(11))
tree.insertNode(Node(10))
tree.insertNode(Node(9))
tree.deleteNode(5)
tree.deleteNode(1)
tree.deleteNode(10)
tree.inOrderTraverse()
