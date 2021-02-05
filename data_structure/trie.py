class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        cur_node.data = string

    def search(self, string):
        cur_node = self.head
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        if cur_node.data != None:
            return True
        else:
            return False

    def start_with(self, prefix):
        cur_node = self.head
        subtrie = None
        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                subtrie = cur_node
            else:
                return False
        queue = list(subtrie.children.values())
        res = []
        while queue:
            cur = queue.pop()
            if cur.data != None:
                res.append(cur.data)

            queue += list(cur.children.values())

        return res
