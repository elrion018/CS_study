

class max_heap:
    def __init__(self):
        self.tree = [0]

    def add(self, value):
        self.tree += [value]
        idx = len(self.tree)-1
        while self.tree[idx] > self.tree[idx//2] and idx != 1:
            self.tree[idx], self.tree[idx //
                                      2] = self.tree[idx//2], self.tree[idx]

            idx = idx//2
        return

    def delete(self):
        self.tree[1], self.tree[len(
            self.tree)-1] = self.tree[len(self.tree)-1], self.tree[1]
        self.tree.pop()
        idx = 1
        while True:
            if 2*idx <= len(self.tree)-1 and self.tree[2*idx] > self.tree[idx] and 2*idx + 1 > len(self.tree)-1:
                self.tree[idx], self.tree[2 *
                                          idx] = self.tree[2*idx], self.tree[idx]
                idx = 2*idx
            elif 2*idx > len(self.tree)-1 and 2*idx + 1 <= len(self.tree)-1 and self.tree[2*idx+1] > self.tree[idx]:
                self.tree[idx]. self.tree[2*idx +
                                          1] = self.tree[2*idx + 1], self.tree[idx]
                idx = 2*idx + 1
            elif 2*idx <= len(self.tree)-1 and 2*idx + 1 <= len(self.tree)-1 and self.tree[2*idx] > self.tree[idx] and self.tree[2*idx+1] > self.tree[idx]:
                if self.tree[2*idx] >= self.tree[2*idx + 1]:
                    self.tree[idx], self.tree[2 *
                                              idx] = self.tree[2*idx], self.tree[idx]
                    idx = 2*idx
                else:
                    self.tree[idx], self.tree[2*idx +
                                              1] = self.tree[2*idx + 1], self.tree[idx]
                    idx = 2*idx + 1
            else:
                break
        return

    def print_heap(self):
        print(self.tree)
        return


heap = max_heap()

heap.add(1)
heap.print_heap()
heap.add(4)
heap.print_heap()
heap.add(6)
heap.print_heap()
heap.add(2)
heap.print_heap()
heap.add(8)
heap.print_heap()
heap.delete()
heap.print_heap()
heap.delete()
heap.print_heap()
heap.delete()
heap.print_heap()
heap.delete()
heap.print_heap()
heap.delete()
heap.print_heap()
