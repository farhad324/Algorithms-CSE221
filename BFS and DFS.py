class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

        
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

    def BFS(self, s):
        visited = set() 
        queue = [] 
        visited.add(s)
        queue.append(s)

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 

            for node in self.graph[s]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        
        
    def DFS(self,s):            
        visited = set()
        stack = []
        stack.append(s)
 
        while (len(stack)):
            s=stack.pop()
            if s not in visited:
                print(s,end=' ')
                visited.add(s)
                
            for node in self.graph[s]:
                if node not in visited:
                    stack.append(node)


V = 6
graph = Graph(V)
graph.add_edge('R', 'M')
graph.add_edge('M', 'N')
graph.add_edge('M', 'Q')
graph.add_edge('Q', 'P')
graph.add_edge('N', 'O')
graph.add_edge('O', 'P')
graph.add_edge('N', 'Q')
print('Breath First Search: ',end='')
graph.BFS('Q')
print()
print('Depth First Search: ',end='')
graph.DFS('Q')
