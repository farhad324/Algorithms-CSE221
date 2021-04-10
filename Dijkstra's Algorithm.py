class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.blocked=[]
 
 
    def add_edge(self, src, dest,weight):
 
        if self.graph.get(src) == None:
            self.graph[src]=[(dest,weight)]
        else:
            self.graph[src]=self.graph.get(src)+[(dest,weight)]
 
 
    def dijkstra(self,src, dst=None):
        
        vertices = []
        for n in self.graph:
            vertices.append(n)
            for v in self.graph[n]:
                vertices +=[v[0]]
 
        queue = set(vertices)
        vertices = list(queue)
        
        dist = {}
        prev = {}
        for n in vertices:
            dist[n] = float('inf')
            prev[n] = None
 
        dist[src] = 0
 
        while queue:
            u = min(queue, key=dist.get)
            queue.remove(u)
 
            if dst is not None and u == dst:
                return dist[dst], prev
 
            for v, w in self.graph.get(u, ()):
                if v in self.blocked:
                    w=float('inf')
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
 
        return dist, prev
 
    def find_path(self,pr, vert): 
        rev = []
        while vert is not None:
            rev.append(vert)
            vert = pr[vert]
        return rev[::-1]
 
    def add_blocked(self,bl):
        self.blocked=bl
 
dest_names={
    0:'Mouchak',1:'Panthapath',2:'Rampura',3:'Shahbagh',
    4:'Dhanmondi',5:'Lalmatia',6:'Badda',7:'Hatirjheel',
    8:'Nilkhet',9:'TSC',10:'Dhaka University',11:'BUET'
}
 
N=int(input())
M=int(input())
 
myGraph = Graph(N)
 
for i in range(M):
    u,v,w = map(int,input().split()) 
    #u,v = map(str,input().split()) ##to take string values
    #w=int(input())
    myGraph.add_edge(u, v,w)    
 
src=int(input()) ## remove int() to take string values
dest=int(input())  ## remove int() to take string values
 
blocked= list(map(int,input().split()))  ## remove int() to take string values
 
myGraph.add_blocked(blocked)
 
cost, prev = myGraph.dijkstra(src, dest)
path = myGraph.find_path(prev, dest)
 
 
for i in path:
    if i==path[0]:
        print("{}".format(dest_names[i]), end="")
    else:
        print("->{}".format(dest_names[i]), end="")
print()
print("Path cost: {}".format(cost))


## INPUT:
'''
12
16
0 1 5
0 2 2
0 3 10
1 4 20
1 5 10
2 6 3
2 7 12
3 8 5
3 9 8
4 11 5
5 10 6
7 8 2
8 10 10
8 11 12
9 11 2
11 10 2
0
10
2 5 6 8

'''

## OUTPUT:

'''
Mouchak->Shahbagh->TSC->BUET->Dhaka University
Path cost: 22

'''
