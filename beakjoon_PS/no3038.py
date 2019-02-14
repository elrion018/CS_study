#노드 클래스
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class ComBinaryTree:
    def __init__(self):
        self.root = None
        self.preorder_list = []
    
    def add(self, item):
        #바이너리 트리에 루트 노드가 없다면
        if self.root is None:
            self.root = Node(item)

        else:
            self._add(self.root, item)


    def _add(self, cur, item):
        if cur.val > item:
            if cur.left is not None:
                self._add(cur.left, item)
            else:
                cur.left = Node(item)
        elif cur.val < item:
            if cur.right is not None:
                self._add(cur.right, item)
            else:
                cur.right = Node(item)
    
    def Pre_order_traversal(self):
        if self.root is not None:
            self.Pre_order(self.root)

    def Pre_order(self, cur): # 프리오더 뿌리노드->왼쪽 서브트리-> 오른쪽 서브트리
        self.preorder_list.append(cur.val)
        if cur.left is not None:
            self.Pre_order(cur.left)
        if cur.right is not None:
            self.Pre_order(cur.right)

N = 0 # 트리의 레벨
num = 0 #노드에 적을 숫자들
dif = 0 #서브트리들의 합의 차





