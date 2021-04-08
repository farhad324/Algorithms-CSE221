class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        
        self.matrix = []
        for i in range(self.V):
            self.matrix.append([0 for i in range(self.V)])
        
    def add_edge(self, src, dest):
        
        ##for adjacency list
        
        if self.graph.get(src) == None:
            self.graph[src]=[dest]
        else:
            self.graph[src]=self.graph.get(src)+[dest]
            
        if self.graph.get(dest) == None:
            self.graph[dest]=[src]
        else:
            self.graph[dest]=self.graph.get(dest)+[src]
        
        ##for adjacency matrix
        
        key_list=list(self.graph.keys())
        
        i1 = key_list.index(src)
        i2 = key_list.index(dest)
        self.matrix[i1][i2] = 1
        self.matrix[i2][i1] = 1
        
    def print_adj_list(self):
        print("Adjacency List: ")
        print()
        for i in self.graph:
            print("Adjacency list of vertex: {}\n head ".format(i), end="")
            for j in self.graph[i]:
                print(" -> {}".format(j), end="")
            print(' \n')
    
        
    def print_adj_matrix(self):     
        print("Adjacency Matrix: ")
        print()
        for i in self.matrix:
            print(i)
            
    
                    
    
V = 5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.print_adj_list()
graph.print_adj_matrix()
print()
print("---------------------------")
print()
V = 5
graph = Graph(V)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')
graph.print_adj_list()
graph.print_adj_matrix()
