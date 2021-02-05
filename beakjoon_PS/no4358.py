import sys


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.num = 0
        self.children = {}


class trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)

            cur = cur.children[char]
        cur.data = string
        cur.num += 1

    def search(self, string):
        cur = self.head
        for char in string:
            if char in cur.children:
                cur = cur.children[char]

            else:
                return False
        if cur.data == string:
            return cur.num
        else:
            return False


arr = []
cnt = 0
_trie = trie()
while True:
    cur = sys.stdin.readline().strip()
    if not cur:
        break
    cnt += 1
    arr.append(cur)
    _trie.insert(cur)
arr = set(arr)
arr = sorted(arr)
for tree in arr:
    print(tree, end=' ')
    print("%.4f" % ((_trie.search(tree) / cnt) * 100))
