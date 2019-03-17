class graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.adj_list = [[] for _ in range(vertex)]
        self.visited_vertex_re = []

    def addEdge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            print("There is edge already!")
            return False
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
    
    def removeEdge(self, v1, v2):
        if v2 not in self.adj_list[v1]:
            print("There is no edge already!")
            return False
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)
    
    def isEdge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            print("There is edge!")
            return True
        else:
            print("There is no edge")
            return False

    def DFS_with_stack(self):
        self.lst = []
        self.stack = []
        for i in self.adj_list:
            self.lst += i
        self.stack.append(min(self.lst))
        self.lst = []
        self.current = 0
        self.visited_vertex = []
        while self.stack:
            self.current = self.stack.pop()
            for neighbor in self.adj_list[self.current]:
                if neighbor not in self.visited_vertex:
                    self.stack.append(neighbor)
            self.visited_vertex.append(self.current)
        return self.visited_vertex

    def BFS_with_queue(self):
        self.lst = []
        self.queue = []
        for i in self.adj_list:
            self.lst += i
        self.queue.append(min(self.lst))
        self.lst = []
        self.current = 0
        self.visited_vertex = []
        while self.queue:
            self.current = self.queue.pop(0)
            for neighbor in self.adj_list[self.current]:
                if neighbor not in self.visited_vertex:
                    self.queue.append(neighbor)
            self.visited_vertex.append(self.current)
        return self.visited_vertex   

    def DFS_recursive(self, vertex):
        self.visited_vertex_re += [vertex]
        for neighbor in reversed(self.adj_list[vertex]):
            if neighbor not in self.visited_vertex_re:
                self.visited_vertex_re = self.DFS_recursive(neighbor)

        return self.visited_vertex_re


            



G = graph(7)
G.addEdge(0,1)
G.addEdge(0,2)
G.addEdge(1,0)
G.addEdge(1,3)
G.addEdge(2,0)
G.addEdge(2,4)
G.addEdge(2,5)
G.addEdge(3,1)
G.addEdge(4,2)
G.addEdge(4,6)
G.addEdge(5,2)
G.addEdge(6,4)
print(G.adj_list)
